# 参数设置
db_path = './db/dbtest.db'                       #链接/新建数据库的地址
input_video_path = './input_videos/test.mp4'     #输入视频文件的位置
production_name = 'test'                         #输入视频所属作品的名称，例如《长风渡》
video_episode = 3                                #输入视频是作品的第几集
video_version = 'v1'                             #输入视频时该集的哪个版本，可以写“删减版、高清版等”

# 引入自定义工具
from myutils import myutils

# 数据库操作
# 链接数据库并初始化，建立数据库对象
myutils.initialiseDB(db_path)                    #初始化数据库
db = myutils.DB(db_path)                         #建立数据库对象实例
# 插入测试数据
try:
    db.insertData('productions',['production_id','production_name'],[('test_id','test')])
    db.insertData('videos',['video_id','production_id','video_id_part','video_episode','video_version'],\
                  [('test_id_0xffff0001','test_id','0xffff0001',1,'v1'),\
                   ('test_id_0xffff0002','test_id','0xffff0002',2,'v1')])
    db.commit()
except:
    pass
db.close()

# 视频操作
# 导入视频，建立视频对象实例，注意这个步骤计算时间长，因为要分析视频的镜头列表
video = myutils.video(input_video_path)
# 将视频拆分、提取关键帧，并将视频的信息导入数据库中
video.video2DB(db_path, production_name, video_episode, video_version,\
               production_background_time='imaginary') 
#前面4个参数为必要参数，后面为可选参数**kwargs，参数名称需要是数据库表中的字段，提供手动信息值