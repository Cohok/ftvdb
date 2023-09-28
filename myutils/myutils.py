# ====================================================================
# myutils包含了调用SQLite3的工具类、调用ffmpeg、scenedetect处理视频文件的类
# 作者：huangpengjie，联系邮箱：380781528@qq.com
# ====================================================================

import sqlite3, scenedetect, ffmpeg, cv2, sys, os, shutil, math, subprocess
import numpy as np
from PIL import Image
from scenedetect import detect, ContentDetector, split_video_ffmpeg, SceneManager, open_video
sys.path.append("..")
from const import scope_tables, db_tables

# 创建数据库类，输入为数据库文件地址
class DB:
    def __init__(self, file_path):
        self.db_name = file_path
        self.conn    = sqlite3.connect(file_path)
        self.cur     = self.conn.cursor()
    ####==================第一部分-表格操作=====================
    def checkTable(self, table_name): #检查TABLE是否存在
    # table_name为文本
    # 引用格式示例：DB.checkTable('table1')
        check = True
        query = "SELECT count(*) FROM sqlite_master WHERE type='table' AND name='%s';" %table_name
        find_tables = self.cur.execute(query).fetchall()[0][0]
        if find_tables == 0: check = False
        return check
    def createTable(self, table_name, column_name, discr): #检查TABLE是否存在，如果不存在创建TABLE
    # table_name为文本，column_name和discr为文本组成的数组
    # 引用格式示例：DB.createTable('table1',['column1','column2'],['TEXT','TEXT'])
        if self.checkTable(table_name) == False:
            query_condition =''
            for i in range(len(column_name)):
                query_condition += column_name[i]
                query_condition += ' '
                query_condition += discr[i]
                if i<len(column_name)-1:
                    query_condition += ',\n'
            query = '''CREATE TABLE %s (%s);\n''' %(table_name,query_condition)
            self.cur.execute(query)
    def deleteTable(self, table_name): #检查表格是否存在，如果存在则删除
    # table_name为文本
        if self.checkTable(table_name) == True:
            query = '''DROP TABLE %s;''' %table_name
            self.cur.execute(query)
    ####===================第二部分-字段操作======================
    def checkColumn(self, table_name, column_name): #检查字段是否存在
    # table_name，column_name都为文本
    # 引用格式示例：DB.checkColumn('table1','column1')
        check = True
        if self.checkTable(table_name) == False: 
            print("TABLE：%s不存在 TABLE: %s not existed" %(table_name,table_name))
            return -1
        else:
            query = "SELECT * FROM sqlite_master WHERE name='%s' AND sql LIKE \x27%%%s%%\x27;" %(table_name, column_name)
            find_columns = self.cur.execute(query).fetchall()
        if find_columns == []: check = False
        return check
    def addColumn(self, table_name, column_name, discr): #检查1个COLUMN是否存在，如果不存在增加COLUMN
    # 每次只能增加一列，不能增加多列
    # table_name，column_name，discr都为文本
    # 引用格式示例：DB.addColumn('table1','column1','TEXT')    
        if self.checkColumn(table_name, column_name) == False:
            query = '''ALTER TABLE %s ADD COLUMN %s %s;''' %(table_name, column_name, discr)
            self.cur.execute(query)
        else:
            print('字段%s已存在 Column %s already existed' %(column_name, column_name))
    def addColumns(self, table_name, column_names, discrs): #检查多个COLUMN是否存在，如果不存在增加COLUMN
    # table_name为文本，column_name和discr为文本组成的数组
    # 引用格式示例：DB.addColumns('table1',['column1','column2'],['TEXT','TEXT'])
        for i in range(len(column_names)):
            self.addColumn(table_name, column_names[i], discrs[i])
    ####===================第三部分-数据操作======================
    def insertData(self, table_name, column_name, data): #插入数据记录
    # table_name为文本
    # column_name为数组，数组内容为文本
    # data为元素是tuple的数组，其中tuple元素为文本，如果只增加一列数据，也必须用tuple，但只写tuple的第一个元素
    # 引用格式示例：DB.insertData('table1',['column1', 'column2'],[('data1',),('data2',)])
        if len(column_name)>0:
            column_name_text = column_name[0]
            for i in range(1, len(column_name)):
                column_name_text += ','
                column_name_text += column_name[i]
            column_take = '?'
            for i in range(len(column_name)-1):
                column_take += ',?'
            query = '''INSERT INTO %s (%s) VALUES (%s);''' %(table_name,column_name_text, column_take)
            self.cur.executemany(query, data)
    def updateData(self, talbe_name, column_name, new_data, *condition): #更新数据库已存在的数据
        # table_name为文本
        # column_name为数组，数组内容为文本
        # new_data为数组，数组的数量要和column_name一样
        # condition为文本
        update_value = ''
        if len(column_name) != len(new_data):
            print("列数量与更新数据数量不同，请检查！")
            return -1
        else:
            for i in range(len(column_name)):
                update_value_i = '%s = %r' %(column_name[i], new_data[i])
                update_value  += update_value_i
        if conditions ==():
            query = '''UPDATE %s SET %s;''' %(table_name, update_value)
        else:
            query = '''UPDATE %s SET %s WHERE %s;''' %(table_name, update_value, condition)
        self.cur.execute(query)
    def select(self, column_name, table_name, *conditions): #查询数据库中的数据
    # column_name为数组，数组内容为文本
    # table_name为文本
    # conditions为文本
        columns = column_name[0]
        for i in range(1, len(column_name)):
            columns += ','
            columns += column_name[i]
        if conditions ==():
            query = '''SELECT %s FROM %s;''' %(columns, table_name)
        else: 
            query = '''SELECT %s FROM %s WHERE %s;''' %(columns, table_name, conditions[0])
        selections = self.cur.execute(query).fetchall()
        return selections
    def dbMergeTool(self, db1_path, db2_path): #数据库合并，把数据db2_path合并到db1_path中，要求结构完全相同
        conn = sqlite3.connect(db1_path)
        conn.text_factory = str
        cur = conn.cursor()
        attach = '''ATTACH DATABASE '%s' as w;''' %db2_path
        cur.execute(attach)
        conn.execute("BEGIN")
        for table in conn.execute("SELECT * FROM w.sqlite_master WHERE type='table'"):
            query = "INSERT INTO %s SELECT * FROM w.%s" %(table[1], table[1])
            conn.execute(query)
        conn.commit()
        conn.execute("DETACH DATABASE w")
        conn.close()
    def dbMerge(self, db_to_merge):
        conn = self.conn
        conn.text_factory = str
        cur = conn.cursor()
        attach = '''ATTACH DATABASE '%s' as w;''' %db_to_merge
        cur.execute(attach)
        conn.execute("BEGIN")
        for table in conn.execute("SELECT * FROM w.sqlite_master WHERE type='table'"):
            query = "INSERT INTO %s SELECT * FROM w.%s" %(table[1], table[1])
            conn.execute(query)
        conn.commit()
        conn.execute("DETACH DATABASE w")
        conn.close()
    ####====================第四部分-数据库操作=======================
    def execute(self, sql_text): #执行输入的sql语句
        self.cur.execute(sql_text)
    def executemany(self, sql_text, data): #执行输入的多条sql语句
        self.cur.executemany(sql_text, data)
    def commit(self): #提交数据记录
        self.conn.commit()
    def close(self): #关闭数据库链接
        self.conn.close()
    ####==================第五部分-影视数据库操作=====================
    def createScopeTables(self): #批量创建范围限定表
        for i in range(scope_tables.tables_count):
            self.createTable(scope_tables.tables_list[i][0], scope_tables.tables_list[i][1], scope_tables.tables_list[i][2])
            self.insertData (scope_tables.tables_list[i][0], scope_tables.tables_list[i][3], scope_tables.tables_list[i][4])
    def refreshAllScopeTables(self): #批量刷新范围限定表
        for i in range(scope_tables.tables_count):
            self.deleteTable(scope_tables.tables_dict[i])
        for i in range(scope_tables.tables_count):
            self.createTable(scope_tables.tables_list[i][0], scope_tables.tables_list[i][1], scope_tables.tables_list[i][2])
            self.insertData (scope_tables.tables_list[i][0], scope_tables.tables_list[i][3], scope_tables.tables_list[i][4])
    def createDBTables(self): #批量初始化创建数据库表
        for i in range(db_tables.tables_count):
            self.createTable(db_tables.tables_list[i][0], db_tables.tables_list[i][1], db_tables.tables_list[i][2])
            self.insertData (db_tables.tables_list[i][0], db_tables.tables_list[i][3], db_tables.tables_list[i][4])

def initialiseDB(db_name): #进行数据库表格初始化
    if os.path.exists(db_name):
        print("同名数据库文件已存在，若要重新初始化请备份后手动删除")
    else:
        db = DB(db_name)
        db.createScopeTables()
        db.createDBTables()
        db.commit()
        db.close()
        print("数据库初始化成功，文件路径：%s" %db_name)


# 创建视频文件对象，输入为视频文件地址、作品名称、视频集序数、[视频版本、production_id]
class video:
    def __init__(self, video_path):
        # *kwargs为输入的与作品、视频文件相关的数据库字段
        self.file_name  = video_path
        self.scene_list = detect(video_path,ContentDetector())
    ####==================第一部分-返回镜头列表=====================
    def getSceneList(self): #返回视频按镜头拆分的结构数据
        return self.scene_list
    def findScenesList(self, threshold=27.0):  #返回视频按镜头拆分的结构数据，增加手动参数，可以调整thereshold精确度
        video = open_video(self.file_name)
        scene_manager = SceneManager()
        scene_manager.add_detector(ContentDetector(threshold=threshold))
        # Detect all scenes in video from current position to end.
        scene_manager.detect_scenes(video)
        # `get_scene_list` returns a list of start/end timecode pairs
        # for each scene that was found.
        return scene_manager.get_scene_list()
    ####==================第二部分-获取信息=====================
    def getVideoInfo(self, *filename): #获取视频文件本身的信息
        info  = {}
        if filename == ():
            probe_file = self.file_name
        else:
            probe_file = filename[0]
        probe = ffmpeg.probe(probe_file) # probe为一个字典，包括'streams'和'format'两个key
        video_format   = probe['format'] #probe['streams']和probe['format']又分别为字典
        video_streams  = probe['streams']
        try:
            video_v_stream = (next(stream for stream in video_streams if stream['codec_type'] == 'video'), None)[0]
        except:
            video_v_stream = {}
        try:
            video_a_stream = (next(stream for stream in video_streams if stream['codec_type'] == 'audio'), None)[0]
        except:
            video_a_stream = {}
        try:
            video_s_stream = (next(stream for stream in video_streams if stream['codec_type'] == 'subtitle'), None)[0]
        except:
            video_a_stream = {}
        # 获取完整的probe信息字符串化记录到info字典的'video_probe'键
        info['video_extension_name'] = self.file_name[self.file_name.rfind(".")+1:]
        info['video_probe'] = str(probe)
        # 获取format字典中的键信息
        try:
            format_keys = list(video_format.keys())
            for key in format_keys:
                info_key = 'video_' + key
                info[info_key] = video_format[key]
                try:
                    info['video_tags'] = str(video_format['tags'])
                    print("video_tags"+ info['tags'] )
                except:
                    pass
            info['format_info'] = 1
        except:
            info['format_info'] = 0
        # 获取stream中video字典中的键信息
        try:
            v_keys = list(video_v_stream.keys())
            for key in v_keys:
                info_key = "video_v_" +key
                info[info_key] = video_v_stream[key]
                try:
                    info['video_v_disposition'] = str(video_v_stream['disposition'])
                except:
                    pass
                try:
                    info['video_v_tags'] = str(video_v_stream['tags'])
                except:
                    pass
            info['v_info'] = 1
        except:
            info['v_info'] = 0
        # 获取stream中audio字典中的键信息
        try:
            a_keys = list(video_a_stream.keys())
            for key in a_keys:
                info_key = "video_a_" + key
                info[info_key] = video_a_stream[key]
                try:
                    info['video_a_disposition'] = str(video_a_stream['disposition'])
                except:
                    pass
                try:
                    info['video_a_tags'] = str(video_a_stream['tags'])
                except:
                    pass
            info['a_info'] = 1
        except:
            info['a_info'] = 0
        # 获取stream中subtitle字典中的键信息
        try:
            s_keys = list(video_s_stream.keys()) #subtitle
            for key in s_keys:
                info_key = "video_s_" + key
                info[info_key] = video_s_stream[key]
                try:
                    info['video_s_disposition'] = str(video_s_stream['disposition'])
                except:
                    pass
                try:
                    info['video_s_tags'] = str(video_s_stream['tags'])
                except:
                    pass
            info['s_info'] = 1
        except:
            info['s_info'] = 0
        return info
    def getDBInfo(self, db_name, production_name, video_episode, video_version, **kwargs): #获取视频文件对应的数据库信息
        # 1. 数据库中id格式：production_id是'0xffffffffffffffff' ，video_id是'0xffffffffffffffff0xffffffff', scene_id是'0xffffffffffffffff0xffffffff0xffffffff'
        # 2.1.1 先在数据库中找production_name的名字，如果存在，返回production_id, 在此前引入production_id_renew参数设定初始为0，代表不更新production_id
        # 2.1.2 引入existance_in_db参数，初始值为0，代表数据库中不存在该视频
        # 2.2 在video TABLE中找video_episode, video_version, 如果同时都一样，说明数据库中已经存在该视频及信息，existance_in_db = 1
        # 2.3 如果existance_in_db = 0，就找到相同production_id下video_id_part中的最大值，在上面加1，作为video_id的video part
        # 3.1 如果production_name在TABLE productions中不存在，那就作把production_id_next作为新文件的production_id，video_id设为0
        # 3.2 将数据库中原本production_id == '0xffffffffffffffff'的数据对应的'production_id_next'加1
        # 4. 文件命名为production_id + "_" + video_id_part + "_" + self.production_name + "_" + str(video_episode) + "_" + video_version
        # 5. 建议输入文件放在input_videos下
        #---------------------------------------------------
        # db_name为文本，是数据库文件的目录，
        # production_name为文本，是作品名称，相同的作品的不同视频文件需要填入相同的作品名称，否则将被认为为两个作品
        # video_episode为作品的集序数，即第几集，数据类型为数
        # video_version是相同作品同一集的不同版本，如高清版、标清版、删减版等，如果只有一个版本，建议设置为“v1”
        
        # 查找production_name，如果找到赋值到production_selection_name，否则production_selection_name为空值
        self.db_name = db_name
        self.production_name = production_name
        self.video_episode = video_episode
        self.video_version = video_version
        dbinfo = {}
        db = DB(db_name)
        production_id_renew = 0
        existance_in_db = 0
        production_selection_id_next = db.select(['production_id_next'],'productions',"production_id == '0xffffffffffffffff'")[0][0]
        try:
            production_selection_id = db.select(['production_id'],'productions','production_name == "%s"' % production_name)[0][0]
        except:
            production_selection_id = ''
        # 如果存在production_name，新文件production_id不更新，并查找video TABLE
        if production_selection_id != '':
            production_id = production_selection_id
            production_id_next =  production_selection_id_next
            try:
            #检查video_episode, video_version，如果输入的值都一样，则提示视频已经存在
                video_selection_episode_version = db.select(['video_id_part'],'videos',"video_episode == %d AND video_version == '%s' " %(video_episode, video_version))[0][0]
                # print('文件已存在于数据库中，video_id：%s' %video_selection_episode_version)
                existance_in_db = 1
                video_id_part = video_selection_episode_version
            except:
            #查找video_id_part中的最大值，在上面加1，作为video_id的video part
                video_selection_id_part = db.select(['video_id_part'],'videos',"production_id == '%s'" %production_id)
                video_selection_id_array = np.array(video_selection_id_part).flatten()
                find_max = []
                for i in range(len(video_selection_id_array)):
                    find_max.append(int(video_selection_id_array[i],16))
                video_id_part = "0x%08x" %int(max(find_max) + 1)
        # 如果没有找到production_name，把production_id_next，并且修改production_id_next
        else:
            production_id = production_selection_id_next
            video_id_part = '0x00000000'
            production_id_renew = 1
            # 修改production_id == '0xffffffffffffffff'的production_id_next，加1
            production_id_next = "0x%08x" %int(int(production_selection_id_next, 16) + 1)
        db.close()
        video_id = production_id + video_id_part
        video_db_name = production_id + "_" + video_id_part + "_" + production_name + "_" + str(video_episode) + "_" + video_version
        video_extension_name = self.file_name[self.file_name.rfind(".")+1:]
        video_db_path = "./multimedia/%s.%s" %(video_db_name, video_extension_name)
        dbinfo['existance_in_db'] = existance_in_db
        dbinfo['production_id_renew'] = production_id_renew
        dbinfo['production_id'] = production_id
        dbinfo['production_id_next'] = production_id_next
        dbinfo['production_name'] = production_name
        dbinfo['video_id_part'] = video_id_part
        dbinfo['video_id'] = video_id
        dbinfo['video_episode'] = video_episode
        dbinfo['video_version'] = video_version
        dbinfo['video_db_name'] = video_db_name
        dbinfo['video_extension_name'] = video_extension_name
        dbinfo['video_filename'] = video_db_path
        dbinfo.update(kwargs)
        self.video_db_name = video_db_name
        self.video_filename = video_db_path
        return dbinfo
    ####==================第三部分-切分镜头操作与镜头数据库信息获取=====================
    def splitVideoTool(self, input_video_path, output_file_template,video_name): #拆分视频文件
        split_video_ffmpeg(input_video_path, self.scene_list, output_file_template, video_name)
    def splitVideo(self):
        videoinfo = self.getVideoInfo()
        scene_dir = './multimedia/%s' %self.video_db_name
        try:
            os.mkdir(scene_dir)
            shutil.copyfile(self.file_name, self.video_filename)
            input_video_path = self.file_name
            output_file_template = '$VIDEO_NAME-Scene-$SCENE_NUMBER.%s' %videoinfo['video_extension_name']
            video_name = '%s/%s' %(scene_dir,self.video_db_name)
            self.splitVideoTool(input_video_path, output_file_template,video_name)
        except:
            pass
    def getSceneDataTool(self, db_name, production_name, video_episode, video_version, scene_squence_number): # 返回一个拆分的镜头视频文件的信息
        sceneinfo = {}
        total_scenes_nb = len(self.scene_list)
        scene_id_part_len = max(int(math.log10(total_scenes_nb)),3)
        dbinfo = self.getDBInfo(db_name, production_name, video_episode, video_version)
        sceneinfo['scene_id_part']          = str(scene_squence_number).rjust(scene_id_part_len,'0')
        sceneinfo['video_id']               = dbinfo['video_id']
        sceneinfo['production_id']          = dbinfo['production_id']
        sceneinfo['scene_id']               = sceneinfo['video_id'] + "-" + sceneinfo['scene_id_part']
        sceneinfo['scene_in_point']         = self.scene_list[scene_squence_number-1][0].get_timecode()
        sceneinfo['scene_out_point']        = self.scene_list[scene_squence_number-1][1].get_timecode()
        sceneinfo['scene_in_point_frame']   = self.scene_list[scene_squence_number-1][0].get_frames()
        sceneinfo['scene_out_point_frame']  = self.scene_list[scene_squence_number-1][1].get_frames()
        sceneinfo['scene_file_name']        = dbinfo['video_db_name'] + '-Scene-'+ sceneinfo['scene_id_part'] + "." + dbinfo['video_extension_name']
        sceneinfo['scene_file_dir']         = "./multimedia/%s/" %dbinfo['video_db_name']
        sceneinfo['scene_file_path']        = sceneinfo['scene_file_dir'] + sceneinfo['scene_file_name']
        try:
            sceneinfo['scene_duration']     = self.getVideoInfo(sceneinfo['scene_file_path'])['video_v_duration']
        except:
            sceneinfo['scene_duration']     = self.getVideoInfo(sceneinfo['scene_file_path'])['video_duration']
        return sceneinfo
    def getSceneData(self, scene_squence_number): # 返回一个拆分的镜头视频文件的信息
        sceneinfo = self.getSceneDataTool(self.db_name, self.production_name, self.video_episode, self.video_version, scene_squence_number)
        return sceneinfo
    ####==================第四部分-关键帧提取操作与帧数据库信息获取=====================
    def getFrameTool(self, file_path, frame_type): #获取关键帧工具
        filename = r'%s' %self.file_name
        command  = 'ffprobe -v error -show_entries frame=pict_type -of default=noprint_wrappers=1'.split()
        out      = subprocess.check_output(command + [file_path]).decode()
        frame_types_list = out.replace('pict_type=', '').split()
        frame_types = zip(range(len(frame_types_list)), frame_types_list)
        type_frames = [x[0] for x in frame_types if x[1] == '%s'%frame_type]
        if type_frames:
            basename = os.path.splitext(os.path.basename(file_path))[0]
            res_dir  = os.path.join(os.path.dirname(file_path), '%s_frames'%basename)
            try:
                os.mkdir(res_dir)
            except:
                pass
            cap = cv2.VideoCapture(file_path)
            for frame_no in type_frames:
                cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
                ret, frame = cap.read()
                outname = basename + '_'+ str(frame_no) + '_' + frame_type + '.jpg'
                if os.path.exists(os.path.join(res_dir, outname)):
                    pass
                else:
                    Image.fromarray(frame).save(os.path.join(res_dir, outname))
            cap.release()
        else:
            print('No %s-frames in'%frame_type + filename)
    def getKeyFrames(self): #获取对象关键帧
        self.getFrameTool(self.video_filename, 'I')
        scene_file_dir = os.path.splitext(self.video_filename)[0]
        scene_file_list = os.listdir(scene_file_dir)
        for file in scene_file_list:
            if file.find("frames")>=0:
                pass
            else:
                file_para_name = r'%s' %(scene_file_dir + '/' + file)
                self.getFrameTool(file_para_name, 'I')
    def keyFramesData2DB(self, db, dir_name, production_id, video_id): #将获取的帧数据写入数据库 
        key_frame_list = os.listdir(dir_name)
        frame_keys = ['frame_id_part', 'frame_id', 'scene_id', 'video_id', 'production_id']
        frame_data = [              0, 'frame_id', 'scene_id',  video_id,   production_id]
        for frame_name in key_frame_list:
            frame_path = os.path.join(dir_name, frame_name)
            frame_name_split = frame_name.split("_")
            frame_id_part = frame_name_split[-2]
            frame_scene_index = frame_name_split[-3].find("Scene")
            if frame_scene_index>0:
                scene_id = video_id + "-" + frame_name_split[-3][frame_scene_index+6:]
            else:
                scene_id = video_id + "-" + "000"
                try:
                    db.insertData('scenes', ['scene_id'], [(scene_id,)]) 
                    db.commit()   
                except:
                    pass
            frame_id = scene_id + "_" + frame_id_part
            try:
                frame_id_selections = db.select(['frame_id_part'],'frames',"frame_id == '%s'" %frame_id)
            except:
                pass
            if frame_id_selections == []:
                frame_data[0] = int(frame_id_part)
                frame_data[1] = frame_id
                frame_data[2] = scene_id
                db.insertData('frames', frame_keys, [tuple(frame_data)])
                db.commit()
    ####========================第五部分-执行操作与数据库更新==========================
    def video2DB(self, db_name, production_name, video_episode, video_version, **kwargs):
        # 执行操作并获取数据
        videodbinfo = {}
        dbinfo = self.getDBInfo(db_name, production_name, video_episode, video_version)
        videoinfo = self.getVideoInfo()
        videodbinfo.update(dbinfo)
        videodbinfo.update(videoinfo)
        videodbinfo.update(kwargs)
        keys_list = list(videodbinfo.keys())
        production_id_next = videodbinfo['production_id_next']
        production_id = videodbinfo['production_id']
        video_id = videodbinfo['video_id']
        if videodbinfo['existance_in_db'] == 0:
            print("开始拆分视频镜头...")
            self.splitVideo()
            print("开始提取关键帧...")
            self.getKeyFrames()
            print("开始获取数据库信息...")
            production_keys = [key for key in keys_list if key[:10]=='production']
            production_keys.remove('production_id_renew')
            production_keys.remove('production_id_next')
            video_keys = [key for key in keys_list if key[:5]=='video']
            video_keys.append('production_id')
            production_data_list = [videodbinfo[key] for key in production_keys]
            production_data = [tuple(production_data_list)]
            video_data_list = [videodbinfo[key] for key in video_keys]
            video_data = [tuple(video_data_list)]
        # 把返回的数据插入数据库中
            db = DB(db_name)
            print("开始写入数据库信息...")
            if videodbinfo['production_id_renew'] == 1:
                db.insertData('productions', production_keys, production_data)
                db.updateData('productions', 'production_id_next', [production_id_next], 'production_id == 0xffffffffffffffff')
            db.insertData('videos', video_keys, video_data)
            db.commit()
            dir_name_1 = './multimedia/%s_frames' %self.video_db_name
            self.keyFramesData2DB(db, dir_name_1, production_id, video_id)
            scenes_count = len(self.scene_list)
            for i in range(1, scenes_count + 1):
                sceneinfo = self.getSceneData(i)
                scene_keys = list(sceneinfo.keys())
                scene_data_list = [sceneinfo[key] for key in scene_keys]
                scene_data = [tuple(scene_data_list)]
                try:
                    db.insertData('scenes', scene_keys, scene_data)
                    db.commit()
                except:
                    pass
                dir_name_i = './multimedia/%s/%s-Scene-%s_frames' %(self.video_db_name, self.video_db_name,sceneinfo['scene_id_part'])
                self.keyFramesData2DB(db, dir_name_i, production_id, video_id)
            db.commit()
            db.close()
            print("完成！")
        else:
            print("数据库中已存在相关视频及信息")

