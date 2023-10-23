# ====================================================================
# myutils包含了调用SQLite3的工具类、调用ffmpeg、scenedetect处理视频文件的类
# 作者：huangpengjie，联系邮箱：380781528@qq.com
# ====================================================================

import sqlite3, scenedetect, ffmpeg, cv2, sys, os, shutil, math, subprocess, csv
import numpy as np
from PIL import Image
from scenedetect import detect, ContentDetector, split_video_ffmpeg, SceneManager, open_video
sys.path.append("..")
from const import scope_tables, db_tables

# 创建数据库类，输入1个文本参数，参数为数据库文件地址，用以做数据库相关操作方法
class DB:
    def __init__(self, db_path):
        self.db_file_path = db_path
        self.db_existance = os.path.exists(db_path)
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()
    ####==============================第一部分-数据库基本操作==============================
    def commit(self): #提交数据记录
        self.conn.commit()
    def close(self): #关闭数据库链接
        self.conn.close()
    ####==============================第二部分-表格TABLE操作==============================
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
                if i < len(column_name)-1:
                    query_condition += ',\n'
            query = '''CREATE TABLE %s (%s);\n''' %(table_name, query_condition)
            self.cur.execute(query)
    def deleteTable(self, table_name): #检查表格是否存在，如果存在则删除
    # table_name为文本
        if self.checkTable(table_name) == True:
            query = '''DROP TABLE %s;''' %table_name
            self.cur.execute(query)
    ####==============================第二部分-字段COLUMN操作==============================
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
    ####==============================第四部分-数据DATA操作==============================
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
    def updateData(self, table_name, column_name, new_data, *conditions): #更新数据库已存在的数据
        # table_name为文本
        # column_name为数组，数组内容为文本
        # new_data为数组，数组的数量要和column_name一样
        # conditions为文本
        update_value = ''
        if len(column_name) != len(new_data):
            print("列数量与更新数据数量不同，请检查！")
            return -1
        else:
            for i in range(len(column_name)):
                update_value_i = '%s = %r ' %(column_name[i], new_data[i])
                update_value  += update_value_i
                if i<len(column_name)-1:
                    update_value  += ","
        if conditions ==():
            query = '''UPDATE %s SET %s;''' %(table_name, update_value)
        else:
            query = '''UPDATE %s SET %s WHERE %s;''' %(table_name, update_value, conditions[0])
        #print(query)
        self.cur.execute(query)
    def dbMergeTool(self, db1_path, db2_path): #数据库合并，把数据db2_path合并到db1_path中，要求结构完全相同的两个.db文件
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
    def dbMerge(self, db_to_merge): #数据库合并，把数据db_to_merge合并到类数据库中，要求结构完全相同的两个.db文件
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
    def export2csv(self, table_name, export_file_path): #导出TABLE到csv文件，解决导出编码乱码问题
        query = 'SELECT * FROM %s' % table_name
        self.cur.execute(query)
        with open(export_file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([i[0] for i in self.cur.description]) #写入表头
            writer.writerows(self.cur)
        self.conn.close()
    ####==============================第五部分-影视数据库操作==============================
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
    def initialiseDB(self): #初始化影视数据库
        try:
            os.mkdir("./multimedia/")
        except:
            pass
        try:
            os.mkdir("./db/")
        except:
            pass
        try:
            os.mkdir("./input_videos/")
        except:
            pass
        try:
            os.remove("./input_videos/存入影视文件")
        except:
            pass
        try:
            os.remove("./db/数据库存放")
        except:
            pass
        try:
            os.remove("./multimedia/（务必删除本文件！）影视文件生成剪裁存放")
        except:
            pass
        if self.db_existance: 
            self.close()
            print("同名数据库文件已存在，若要重新初始化请备份后手动删除")
        else:
            self.createScopeTables()
            self.createDBTables()
            self.commit()
            self.close()
            print("数据库初始化成功，文件路径：%s" % self.db_file_path)


#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
# 创建数据库类，输入1个文本参数，参数为视频文件地址，用以做视频相关操作方法
class Video:
    def __init__(self, video_path):
        self.video_input_file_path = video_path
        self.video_input_file_basename = os.path.splitext(os.path.basename(video_path))[0]
        self.video_input_file_extensionname = os.path.splitext(os.path.basename(video_path))[1]
        self.video_input_file_dir = os.path.dirname(video_path)
    ####==============================第一部分-获取视频镜头、帧列表==============================
    def getScenesList(self):
        self.scenes_list = detect(self.video_input_file_path,ContentDetector())
        return self.scenes_list
    def getFramesListTool(self, video_input_file_path):
    # input_file_path为文本，输入文件的地址
    # 方法结果返回数组，为帧排序列示IPB
        filename = r'%s' % video_input_file_path
        command = 'ffprobe -v error -show_entries frame=pict_type -of default=noprint_wrappers=1'.split()
        out = subprocess.check_output(command + [filename]).decode()
        frames_list = out.replace('pict_type=', '').split()
        return frames_list
    def getFramesTypeListTool(self, video_input_file_path, frame_type):
    # input_file_path为文本，输入文件的地址
    # frame_type为文本，只能选择"I"（关键帧，帧内编码帧intra picture）,"P"（前向预测编码帧predictive-frame),"B"(双向预测内插编码帧bi-directionalinterpolated prediction frame)
    # 方法结果返回数组，为frame_type在列中的序号（第1帧从0开始）
        frames_list = self.getFramesListTool(video_input_file_path)
        frames_zip  = zip(range(len(frames_list)), frames_list)
        frames_type_list = [x[0] for x in frames_zip if x[1] == '%s' % frame_type]
        return frames_type_list
    def getFramesList(self):
    # 仅返回对象本身的帧序列表
        return self.getFramesListTool(self.video_input_file_path)
    def getFramesTypeList(self, frame_type):
    # 仅返回对象本身的关键帧序数列表
        return self.getFramesTypeListTool(self.video_input_file_path, frame_type)
    ####==============================第二部分-视频镜头切分==============================
    def splitVideoTool(self, scene_file_dir, scenes_list, video_db_file_extensionname, video_db_file_basename): #拆分视频文件
        try:
            os.mkdir(scene_file_dir)
        except:
            pass
        output_file_template = '$VIDEO_NAME%sScene%s$SCENE_NUMBER%s' % ("-","-",video_db_file_extensionname)
        video_name = '%s/%s' % (scene_file_dir, video_db_file_basename)
        input_video_path = scene_file_dir + video_db_file_extensionname
        split_video_ffmpeg(input_video_path, scenes_list, output_file_template, video_name)
        # 在DBVideo子类调用中，使用self.splitVideoTool(self.scene_file_dir, scenes_list, self.video_db_file_extensionname, self.video_db_file_basename)
    def splitVideo(self):
        scene_file_dir = "%s/%s" % (self.video_input_file_dir, self.video_input_file_basename)
        try:
            os.mkdir(scene_file_dir)
        except:
            pass
        input_video_path = self.video_input_file_path
        scenes_list = self.getScenesList()
        output_file_template = '$VIDEO_NAME%sScene%s$SCENE_NUMBER%s' % ("-","-",self.video_input_file_extensionname)
        video_name = '%s/%s' % (scene_file_dir, self.video_input_file_basename)
        split_video_ffmpeg(input_video_path, scenes_list, output_file_template, video_name)        
    ####==============================第三部分-视频帧提取==============================
    def getFramesTool(self, video_input_file_path, frame_type):
        frames_type_list = self.getFramesTypeListTool(video_input_file_path, frame_type)
        if frames_type_list: # 如果获取的列表不为空
            basename = os.path.splitext(os.path.basename(video_input_file_path))[0]
            res_dir  = os.path.join(os.path.dirname(video_input_file_path), '%s_frames'% basename)
            try:
                os.mkdir(res_dir)
            except:
                pass
            cap = cv2.VideoCapture(video_input_file_path)
            for frame_no in frames_type_list:
                cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
                ret, frame = cap.read()
                frame[:,:,[0,1,2]]=frame[:,:,[2,1,0]] #存储格式由BGR转为RGB
                #print(frame)
                outname = basename + '_' + str(frame_no) + '_' + frame_type + '.jpg'
                if os.path.exists(os.path.join(res_dir, outname)):
                    pass
                else:
                    Image.fromarray(frame).save(os.path.join(res_dir, outname))
            cap.release()
            pass
        else:
            print('No %s-frames in %s'% (frame_type, video_input_file_path))
    def getKeyFramesTool(self, video_input_file_path):
        self.getFramesTool(video_input_file_path, "I")
    def getScenesKeyFrames(self, scene_file_dir):
        scene_file_list = os.listdir(scene_file_dir)
        for file in scene_file_list:
            if file.find("frames")>=0:
                pass
            else:
                file_para_name = r'%s' %(scene_file_dir + '/' + file)
                self.getFramesTool(file_para_name, 'I')
    ####==============================第四部分-读取视频数据信息==============================
    def getVideoInfo(self, *filename): #获取视频文件本身的信息
        info  = {}
        if filename == ():
            probe_file = self.video_input_file_path
        else:
            probe_file = filename[0]
        probe = ffmpeg.probe(probe_file) # probe为一个字典，包括'streams'和'format'两个key
        video_format   = probe['format'] # probe['streams']和probe['format']又分别为字典
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
        info['video_probe'] = str(probe)
        # 获取format字典中的键信息
        try:
            format_keys = list(video_format.keys())
            for key in format_keys:
                info_key = 'video_' + key
                info[info_key] = video_format[key]
                try:
                    info['video_tags'] = str(video_format['tags'])
                    # print("video_tags"+ info['tags'] )
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

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
# 创建同时继承Class DB和Class Video的子类DBVideo，处理视频与数据库的交集方法在这里定义
class DBVideo(DB, Video):
    def __init__(self, db_path, video_path, production_category, production_name, video_episode, video_version, **kwargs):
        DB.__init__(self, db_path)
        Video.__init__(self, video_path)
        self.production_category = production_category
        self.production_name = production_name
        self.video_episode = video_episode
        self.video_version = video_version
        self.kwargs = kwargs
        # 设置可变参数的默认值
        self.video_data_existance_in_db = 0
        self.production_id_renew = 0
        # 查找数据库中的值，并赋值给类中的全局参数
        self.selection_production_id_next = self.select(['production_id_next'],'productions','production_id == "0xffffffffffffffff"')[0][0]
        try:
            self.selection_production_id = self.select(['production_id'],'productions','production_name == "%s"' % production_name)[0][0]
        except:
            self.selection_production_id = ''
        # 赋值self.production_id,self.production_id_next,self.production_id_renew
        # 如果存在production_name，新文件production_id不更新，并查找video TABLE，判断唯一识别video_id对应的video_id_part是否存在
        if self.selection_production_id != '':
            self.production_id = self.selection_production_id
            self.production_id_next = self.selection_production_id_next
            try:
                self.selection_video_id_part = self.select(['video_id_part'],'videos','video_episode == "%s" AND video_version == "%s" AND production_id == "%s"' % (video_episode, video_version, self.production_id))[0][0]
            except:
                self.selection_video_id_part = ''
            # 检查video_episode, video_version，如果和输入的值都一样，则可以返回一个有值的selection_video_id_part，视频数据已经存在于数据库表
            if self.selection_video_id_part != '':
                self.video_data_existance_in_db = 1
                self.video_id_part = self.selection_video_id_part
            # 如果selection_video_id_part为空，则对象是已存在的production下的不同视频，视频数据在没在数据库中，开始赋值self.video_id_part
            else:
                selection_video_id_part_list = self.select(['video_id_part'],'videos',"production_id == '%s'" % self.production_id)
                selection_video_id_part_array = np.array(selection_video_id_part_list).flatten()
                find_max = []
                for i in range(len(selection_video_id_part_array)):
                    find_max.append(int(selection_video_id_part_array[i],16))   
                self.video_id_part = "0x%08x" %int(max(find_max) + 1) # 08位十六进制表达
        # 如果没有找到production_name，说明是新的作品，把selection_production_id_next值赋给production_id，并且更新production_id_next
        else:
            self.production_id = self.selection_production_id_next
            self.video_id_part = '0x00000000'
            self.production_id_renew = 1
            # 修改production_id == '0xffffffffffffffff'的production_id_next，加1
            self.production_id_next = "0x%016x" %int(int(self.selection_production_id_next, 16) + 1)
        # 通过上面的条件判断得到了self.production_id,self.video_id_part,self.production_id_renew,self.production_id_next,self.video_data_existance_in_db
        self.video_id = self.production_id + "_" + self.video_id_part
        self.video_db_file_basename = self.video_id + "_" + self.production_name + "_" + str(self.video_episode) + "_" + self.video_version
        self.video_db_file_extensionname = self.video_input_file_extensionname
        self.video_db_file_dir = "./multimedia/"
        self.video_db_file_path = os.path.join(self.video_db_file_dir, self.video_db_file_basename + self.video_db_file_extensionname)
        self.video_db_file_existance = os.path.exists(self.video_db_file_path)
        # 为镜头和帧指定目录
        self.scene_file_dir = self.video_db_file_dir + self.video_db_file_basename
        self.frame_file_dir = self.video_db_file_dir + self.video_db_file_basename + "_frames/"
    def checkTasks(self):
        # 默认所有任务都要执行
        mv_rename_task = 1
        split_video_task = 1
        get_frames_task = 1
        productions_TABLE_task = 1
        videos_TABLE_task = 1
        scenes_TABLE_task = 1
        frames_TABLE_task = 1
        print('0. 正在读取"%s"视频内容' % self.video_input_file_path)
        scenes_list = self.getScenesList()
        key_frames_list = self.getFramesTypeList("I")
        print("0. 读取完成")
        # 检查重命名视频文件是否存在，如果不存在，则后续需要执行重命名和移动文件并且切分镜头提取帧，否则不移动重命名文件单独检查是否需要切分镜头
        print("1. 检查是否进行文件移动与重命名任务：")
        if self.video_db_file_existance:
            print("1. 检查结果：不执行该任务")
            mv_rename_task = 0
            # 在重命名文件存在的情况下，检查是否存在已切分的镜头文件，如果不存在，则后续需要切分镜头
            print("2. 检查是否进行视频镜头切分任务：")
            scene_file_amount = os.listdir(self.scene_file_dir) 
            for item in scene_file_amount:
                if '_frame' in item:
                    scene_file_amount.remove(item)
            if len(scene_file_amount) == len(scenes_list):
                print("2. 检查结果：不执行该任务")
                split_video_task = 0
            else: 
                print("2. 检查结果：执行该任务")
            # 仅仅在重命名视频文件存在且切分视频也存在的情况下，检查是否提取帧，否则默认执行提取帧
            print("3. 检查是否进行提取关键帧任务：")
            try:
                frame_file_amount = os.listdir(self.frame_file_dir)
                if len(frame_file_amount) == len(key_frames_list):
                    print("3. 检查结果：不执行该任务")
                    get_frames_task = 0
                else:
                    print("3. 检查结果：执行该任务")
            except:
                print("3. 检查结果：执行该任务")
        else:
            # 在重命名文件不存在的情况下默认不检查直接执行切分镜头、提取关键帧任务
            print("1. 检查结果：执行该任务\n2-3. 默认执行镜头切分任务、提取关键帧任务")
        # 检查是否写入productions TABLE数据
        print("4. 检查是否进行productions TABLE数据写入任务：")
        if self.production_id_renew == 1:
            print("4. 检查结果：执行该任务")
        else:
            print("4. 检查结果：不执行该任务")
            productions_TABLE_task = 0
        # 检查是否写入videos TABLE数据
        print("5. 检查是否进行videos TABLE数据写入任务：")
        if self.video_data_existance_in_db == 0:
            print("5. 检查结果：执行该任务")
        else:
            print("5. 检查结果：不执行该任务")
            videos_TABLE_task = 0
        # 检查是否写入scenes TABLE数据
        print("6. 检查是否进行scenes TABLE数据写入任务：")
        scene_data_list = np.array(self.select(['scene_id'],'scenes','video_id == "%s"' % self.video_id)).flatten()
        if len(scene_data_list) == len(scenes_list):
            print("6. 检查结果：不执行该任务")
            scenes_TABLE_task = 0
        else:
            print("6. 检查结果：执行该任务")
        # 检查是否写入frames TABLE数据
        print("7. 检查是否进行frames TABLE数据写入任务：")
        try:
            frame_file_amount = os.listdir(self.frame_file_dir)
        except:
            frame_file_amount = []
        if len(key_frames_list) != len(frame_file_amount):
            print("7. 检查结果：执行该任务")
        else:
            if len(os.listdir(self.scene_file_dir)) == 2*len(scenes_list):
                print("7. 检查结果：不执行该任务")
                frames_TABLE_task = 0
            else:
                print("7. 检查结果：执行该任务")
        # 汇总检查结果
        tasks =[mv_rename_task, split_video_task, get_frames_task, productions_TABLE_task, videos_TABLE_task, scenes_TABLE_task, frames_TABLE_task]
        print("******共需执行%d个任务******" % sum(tasks))
        return tasks, scenes_list, key_frames_list
    def mvAndRename(self):
        shutil.copyfile(self.video_input_file_path, self.video_db_file_path)
    def getProductionsData(self):
        production_data_dict = {}
        production_data_dict['production_id'] = self.production_id
        production_data_dict['production_category'] = self.production_category
        production_data_dict['production_name'] = self.production_name
        production_data_dict.update(self.kwargs)
        production_data_dict_keys_list = list(production_data_dict.keys())
        production_data_keys = [key for key in production_data_dict_keys_list if key[:10]=='production']
        production_data_values = [tuple([production_data_dict[key] for key in production_data_keys])]
        return production_data_keys, production_data_values
    def productionsData2DB(self):
        production_keys, production_data = self.getProductionsData()
        self.insertData('productions', production_keys, production_data)
        self.updateData('productions', ['production_id_next'], [self.production_id_next], 'production_id == "0xffffffffffffffff"')
        self.commit()
    def getVideosData(self):
        video_data_dict = self.getVideoInfo()
        video_data_dict['video_episode'] = self.video_episode
        video_data_dict['video_version'] = self.video_version
        video_data_dict['video_id'] = self.video_id
        video_data_dict['video_id_part'] = self.video_id_part
        video_data_dict['production_id'] = self.production_id
        video_data_dict['video_db_file_basename'] = self.video_db_file_basename
        video_data_dict['video_db_file_extensionname'] = self.video_db_file_extensionname
        video_data_dict['video_db_file_dir'] = self.video_db_file_dir
        video_data_dict['video_db_file_path'] = self.video_db_file_path
        video_data_dict.update(self.kwargs)
        video_data_dict_keys_list = list(video_data_dict.keys())
        video_data_keys =[key for key in video_data_dict_keys_list if key[:5]=='video']
        video_data_keys.append('production_id')
        video_data_values = [tuple([video_data_dict[key] for key in video_data_keys])]
        return video_data_keys, video_data_values
    def videosData2DB(self):
        video_data_keys, video_data_values = self.getVideosData()
        self.insertData('videos', video_data_keys, video_data_values)
        self.commit()     
    def getScenesDataTool(self, scenes_list, scene_squence_number):
        scene_data_dict = {}
        scene_total_nb  = len(scenes_list)
        scene_id_part_len = max(int(math.log10(scene_total_nb))+1, 3)
        scene_data_dict['scene_id_part'] = str(scene_squence_number).rjust(scene_id_part_len,'0')
        scene_data_dict['video_id'] = self.video_id
        scene_data_dict['production_id'] = self.production_id
        scene_data_dict['scene_id'] = self.video_id + "_" + scene_data_dict['scene_id_part']
        scene_data_dict['scene_in_point'] = scenes_list[scene_squence_number-1][0].get_timecode()
        scene_data_dict['scene_out_point'] = scenes_list[scene_squence_number-1][1].get_timecode()
        scene_data_dict['scene_in_point_frame'] = scenes_list[scene_squence_number-1][0].get_frames()
        scene_data_dict['scene_out_point_frame'] = scenes_list[scene_squence_number-1][1].get_frames()
        scene_data_dict['scene_file_basename'] = self.video_db_file_basename + '-Scene-' + scene_data_dict['scene_id_part']
        scene_data_dict['scene_file_extensionname'] = self.video_db_file_extensionname
        scene_data_dict['scene_file_dir'] = self.scene_file_dir
        scene_data_dict['scene_file_path'] = os.path.join(self.scene_file_dir,scene_data_dict['scene_file_basename']+self.video_db_file_extensionname)
        try:
            try:
                scene_data_dict['scene_duration'] = self.getVideoInfo(scene_data_dict['scene_file_path'])['video_v_duration']
            except:
                scene_data_dict['scene_duration'] = self.getVideoInfo(scene_data_dict['scene_file_path'])['video_duration']
        except:
            scene_data_dict['scene_duration'] = 0.0
        scene_data_dict['scene_scenery_1'] = ''
        scene_data_dict['scene_scenery_2'] = ''
        scene_data_dict['scene_scenery_3'] = ''
        return scene_data_dict
    def scenesData2DB(self, scenes_list):
        scenes_count = len(scenes_list)
        for i in range(1, scenes_count + 1):
            scene_data_dict = self.getScenesDataTool(scenes_list, i)
            scene_data_keys = list(scene_data_dict.keys())
            scene_data_values = [tuple([scene_data_dict[key] for key in scene_data_keys])]
            try:
                self.insertData('scenes', scene_data_keys, scene_data_values)
                self.commit()
            except:
                pass
            self.framesData2DBTool(scene_data_dict['scene_file_path'], 'I', scene_data_dict['scene_id'])
    def getFramesDataTool(self, video_input_file_path, frame_type, scene_id, frame_id_part, frame_sequence_nb): # 获取单帧的信息方法工具
        frame_data_dict = {}
        frame_data_dict['frame_id_part'] = frame_id_part
        videobasename = os.path.splitext(os.path.basename(video_input_file_path))[0]
        frame_data_dict['frame_file_dir'] = os.path.join(os.path.dirname(video_input_file_path), '%s_frames'% videobasename)
        if scene_id == 0:
            frame_data_dict['frame_file_basename'] = videobasename + '-Scene-000_' + str(frame_sequence_nb) + '_' + frame_type + '.jpg'
            frame_data_dict['scene_id'] = self.video_id + "_000"
        else: 
            frame_data_dict['frame_file_basename'] = videobasename + '_' + str(frame_sequence_nb) + '_' + frame_type + '.jpg'
            frame_data_dict['scene_id'] = scene_id
        frame_data_dict['frame_id'] = frame_data_dict['scene_id'] + "_" + str(frame_id_part)
        frame_data_dict['video_id'] = self.video_id
        frame_data_dict['production_id'] = self. production_id
        frame_data_dict['frame_sequence_nb'] = frame_sequence_nb
        frame_data_dict['frame_file_extensionname'] = 'jpg'
        frame_data_dict['frame_file_path'] = os.path.join(frame_data_dict['frame_file_dir'], frame_data_dict['frame_file_basename'])
        return frame_data_dict
    def framesData2DBTool(self, video_input_file_path, frame_type, scene_id, *given_frames_list):
        if given_frames_list == ():
            frames_list = self.getFramesTypeListTool(video_input_file_path, frame_type)
        else:
            frames_list = given_frames_list[0]
        frames_id_part_len = max(int(math.log10(len(frames_list)))+1, 3)
        for i, frame_nb in enumerate(frames_list):
            frame_id_part = str(i+1).rjust(frames_id_part_len,'0')
            frame_data_dict = self.getFramesDataTool(video_input_file_path, frame_type, scene_id, frame_id_part, frame_nb)
            frame_data_keys = list(frame_data_dict.keys())
            frame_data_values = [tuple([frame_data_dict[key] for key in frame_data_keys])]
            self.insertData('frames', frame_data_keys, frame_data_values)
            self.commit()
    def framesData2DB(self, frames_list):
        self.framesData2DBTool(self.video_db_file_path, 'I', 0, frames_list)
    def checkAndVideo2DB(self):
        # 检查任务是否执行
        tasks, scenes_list, key_frames_list = self.checkTasks()
        # 按照是否执行7个操作逐个执行
        if tasks[0] == 1:
            print("1. 正在移动并重命名文件...")
            self.mvAndRename()
            self.video_db_file_existance = 1
            print("1. 完成视频文件入库，文件路径：%s" % self.video_db_file_path)
        if tasks[1] == 1:
            print("2. 正在进行视频镜头切分...")
            self.splitVideoTool(self.scene_file_dir, scenes_list, self.video_db_file_extensionname, self.video_db_file_basename)
            print("2. 完成视频镜头文件入库，文件目录：%s" % self.scene_file_dir)
        if tasks[2] == 1:
            print("3. 正在进行关键帧提取...")
            self.getKeyFramesTool(self.video_db_file_path)
            self.getScenesKeyFrames(self.scene_file_dir)
            print("3. 完成关键帧文件入库，文件目录：%s" % self.frame_file_dir)
        if tasks[3] == 1:
            print("4. 正在写入productions TABLE数据...")
            self.productionsData2DB()
            self.production_id_renew = 0
            print("4. productions TABLE数据写入完成")
        if tasks[4] == 1:
            print("5. 正在写入videos TABLE数据...")
            self.videosData2DB()
            self.video_data_existance_in_db = 1
            print("5. videos TABLE数据写入完成")
        if tasks[5] == 1:
            print("6.正在写入scenes TABLE数据...")
            self.scenesData2DB(scenes_list)
            print("6. scenes TABLE数据写入完成")
        if tasks[6] == 1:
            print("7. 正在写入frames TABLE数据...")
            self.framesData2DB(key_frames_list)
            print("7. frames TABLE数据写入完成")
    def Video2DB(self, *silent):
        try:
            silence = silent.index('silent')
        except:
            silence = -1
        print("正在读取视频文件信息：%s" %self.video_input_file_path)
        scenes_list = self.getScenesList()
        key_frames_list = self.getFramesTypeList("I")
        if silence == -1:
            print("1. 正在移动并重命名文件...")
        self.mvAndRename()
        self.video_db_file_existance = 1
        if silence == -1:
            print("1. 完成视频文件入库，文件路径：%s" % self.video_db_file_path)
        if silence == -1:
            print("2. 正在进行视频镜头切分...")
        self.splitVideoTool(self.scene_file_dir, scenes_list, self.video_db_file_extensionname, self.video_db_file_basename)
        if silence == -1:    
            print("2. 完成视频镜头文件入库，文件目录：%s" % self.scene_file_dir)
        if silence == -1:
            print("3. 正在进行关键帧提取...")
        self.getKeyFramesTool(self.video_db_file_path)
        self.getScenesKeyFrames(self.scene_file_dir)
        if silence == -1:
            print("3. 完成关键帧文件入库，文件目录：%s" % self.frame_file_dir)
        if self.production_id_renew == 1:
            if silence == -1:
                print("4. 正在写入productions TABLE数据...")
            self.productionsData2DB()
            self.production_id_renew = 0
            if silence == -1:    
                print("4. productions TABLE数据写入完成")
        if silence == -1:
            print("5. 正在写入videos TABLE数据...")
        self.videosData2DB()
        self.video_data_existance_in_db =1
        if silence == -1:
            print("5. videos TABLE数据写入完成")
        if silence == -1:
            print("6.正在写入scenes TABLE数据...")
        self.scenesData2DB(scenes_list)
        if silence == -1:
            print("6. scenes TABLE数据写入完成")
        if silence == -1:
            print("7. 正在写入frames TABLE数据...")
        self.framesData2DB(key_frames_list)
        if silence == -1:
            print("7. frames TABLE数据写入完成")