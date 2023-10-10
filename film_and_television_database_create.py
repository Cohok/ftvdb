### 数据库操作

# 引入自定义工具
from myutils import myutils
db_path = './db/ftvdb.db'                       #链接/新建数据库的地址
# 建立数据库对象
db = myutils.DB(db_path)                         #建立数据库对象实例
db.initialiseDB()                                #初始化数据库

### 连续操作
# 《长风渡》
production_name = '长风渡'                                   #输入视频所属作品的名称，例如《长风渡》
production_category = '电视剧'                               #输入作品类型
video_version = 'v1'                                         #输入视频时该集的哪个版本，可以写“删减版、高清版等”
for i in range(1,41):
    video_episode = i                                                #输入视频是作品的第几集
    input_video_path = './input_videos/长风渡/长风渡-%02d.mkv'%i      #输入视频文件的位置
    # 导入视频，建立视频对象实例
    video = myutils.DBVideo(db_path, input_video_path, production_category, production_name, video_episode, video_version,\
                            production_background_time='虚构、古代', production_total_esipodes=40,\
                            production_filming_time='2022年',production_release_time='2023-06-18',\
                            production_background_place='虚构',production_novel_based=1, production_color=1,\
                            production_plot_outline='讲述了自小受尽磨砺的扬州布商之女柳玉茹与当地著名纨绔顾九思阴差阳错结为夫妻性格迥异的两人在错位婚姻里从相互抵触到相互扶持相互治愈的暖心故事',\
                            production_douban_average_user_rating=6.5)
    # 将视频拆分、提取关键帧，并将视频的信息导入数据库中
    video.Video2DB('silent')

# 《鹊刀门传奇》
production_name = '鹊刀门传奇'                               #输入视频所属作品的名称
production_category = '电视剧'                               #输入作品类型
video_version = 'v1'                                         #输入视频时该集的哪个版本，可以写“删减版、高清版等”
for i in range(1,41):
    video_episode = i                                                       #输入视频是作品的第几集
    input_video_path = './input_videos/鹊刀门传奇/鹊刀门传奇%02d.mkv'%i     #输入视频文件的位置
    # 导入视频，建立视频对象实例
    video = myutils.DBVideo(db_path, input_video_path, production_category, production_name, video_episode, video_version,\
                            production_background_time='虚构、古代', production_total_esipodes=40,\
                            production_filming_time='2022年',production_release_time='2023-08-18',\
                            production_background_place='虚构',production_novel_based=1, production_color=1,\
                            production_plot_outline='某朝末年，倭乱四起，宦官专权，东厂曹公公勾结倭寇，残害中原武林，意欲谋反。长海对外身份是鹊刀门掌门，实则是秘密抗倭组织成员，除了剿灭倭寇，另一项重要任务就是查出勾结倭寇的朝中汉奸。而同时曹公公也发现有反对自己的武林人士存在，暗中派人监视武林各门派的一举一动。因要掩人耳目，并同时进行秘密任务，西门长海找到远在家乡的孪生兄弟西门长在，让他，冒充自己。虽是孪生兄弟，西门长海和西门长在兄弟俩的个性和人生道路完全不同，弟弟是英雄虎胆的一代大侠，哥哥则是胆小懦弱的市井伙夫。面对弟弟的请求，胆小怕事的西门长在一万个不答应，奈何顶住了弟弟长海的威逼利诱，却顶不住弟弟许诺给他找个“老伴”的色诱，于是半推半就的同意冒名顶替。就这样，西门长在稀里糊涂的从一个掌勺摇身一变成为掌门，进入了光怪陆离的武侠世界。西门长在来到人生地不熟的鹊刀门，想要冒充弟弟，首先遇到的第一关，就是要骗过弟弟长海身边的几位亲人：呆傻木讷的大徒弟郝盟和性如烈火的叶四娘，鲁莽冲动的二徒弟赵德柱，当然最难的是弟弟的女儿西门柔。西门长在本来想低调蒙混过关，不料树欲静却风不止，各自风波接踵而来，天池帮帮主高大毛，五毒教教主等人纷纷找上门来，最危险的是，西门长在引起了东厂曹公公的注意和怀疑！',\
                            production_douban_average_user_rating=8.1)
    # 将视频拆分、提取关键帧，并将视频的信息导入数据库中
    video.Video2DB('silent')

# 《长相思》
production_name = '长相思'                                   #输入视频所属作品的名称
production_category = '电视剧'                               #输入作品类型
video_version = 'v1'                                         #输入视频时该集的哪个版本，可以写“删减版、高清版等”
for i in range(1,41):
    video_episode = i                                                       #输入视频是作品的第几集
    input_video_path = './input_videos/长相思/长相思%02d.mkv'%i             #输入视频文件的位置
    # 导入视频，建立视频对象实例
    video = myutils.DBVideo(db_path, input_video_path, production_category, production_name, video_episode, video_version,\
                            production_other_name_1 = 'Lost You Forever',\
                            production_background_time='虚构、神话', production_total_esipodes=40,\
                            production_filming_time='2022年',production_release_time='2023-07-24',\
                            production_background_place='虚构、神话',production_novel_based=1, production_color=1,\
                            production_plot_outline='大荒内，人、神、妖混居，西炎、辰荣、皓翎三国鼎立。流落大荒的皓翎国王姬玖瑶（小夭）历经百年颠沛之苦，不但失去了身份，也失去了容貌，在清水镇落脚，成为了“无处可去、无人可依、无力自保”的玟小六。他悬壶为生恣意不羁。曾与小夭青梅竹马的西炎国王孙玱玹去了皓翎国做质子，即使寄人篱下、隐忍蛰伏，为了寻找小夭走遍大荒，来到清水镇。清水镇的日子平淡温馨，玟小六意外救了垂危的青丘公子涂山璟，朝夕相处中二人情愫渐生；玟小六又与九头妖相柳不打不相识，惺惺相惜结为知己。玟小六和玱玹相见不相识，几经波折，才终与玱玹相认，恢复王姬身份。为了一统天下，玱玹舍私情要王座，相柳守义战死、小夭帮助玱玹完成大业后，与涂山璟隐逸江湖。思而不得的玱玹将所有精力都放在了治理国家上，因为他知道，只要天下太平，他的小夭就能够幸福安康。',\
                            production_douban_average_user_rating=7.7)
    # 将视频拆分、提取关键帧，并将视频的信息导入数据库中
    video.Video2DB('silent')

### 单视频操作
# input_video_path = './input_videos/test.mp4'                 #输入视频文件的位置
# production_name = '长风渡'                                   #输入视频所属作品的名称，例如《长风渡》
# production_category = '电视剧'                               #输入作品类型
# video_episode = 1                                            #输入视频是作品的第几集
# video_version = 'v1'                                         #输入视频时该集的哪个版本，可以写“删减版、高清版等”
# videos = myutils.DBVideo(db_path, input_video_path, production_category, production_name, video_episode, video_version,\
#                          production_background_time='虚构、古代',\
#                          production_total_esipodes=40, production_filming_time='2022年',\
#                          production_release_time='2023-06-18', production_background_place='虚构',\
#                          production_novel_based=1, production_color=1,\
#                          production_plot_outline='讲述了自小受尽磨砺的扬州布商之女柳玉茹与当地著名纨绔顾九思阴差阳错结为夫妻性格迥异的两人在错位婚姻里从相互抵触到相互扶持相互治愈的暖心故事',\
#                          production_douban_average_user_rating=6.5)
# videos.checkAndVideo2DB()