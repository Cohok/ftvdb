# ====================================================================
# scope_tables包含了数据库范围限定表的创建信息，作为常数信息
# 作者：huangpengjie，联系邮箱：380781528@qq.com
# ====================================================================
tables_count = 0
tables_dict  = {}
tables_list  = []

#添加一张表的信息就使用下面一段完整的代码
# tables_list.append(['',[],[],[],[]])
# tables_list[tables_count][0]='table_name' # 表格名称
# tables_list[tables_count][1]=['column1']  # 表格所有列的名
# tables_list[tables_count][2]=['TEXT']		# 表格所有列的描述
# tables_list[tables_count][3]=tables_list[tables_count][1] #表格初始化填入数据的列
# tables_list[tables_count][4]=[('data1',),('data2',),('data3',),('data4',),('data5',),('data6',)] #表格初始化数据
# tables_dict[tables_count]=tables_list[tables_count][0]
# tables_count += 1

# -------------------------以下为production表字段限定范围-------------------------
#scope_production_category：作品分类
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='scope_production_category'
tables_list[tables_count][1]=['production_category']
tables_list[tables_count][2]=['TEXT']
tables_list[tables_count][3]=tables_list[tables_count][1]
tables_list[tables_count][4]=[('电影',),('电视剧',),('纪录片',),('动画',),('综艺节目',),('其他',)]
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1


#scope_production_genre_Robert_McKeey：罗伯特·麦基作品类型
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='scope_production_genre_Robert_McKeey'
tables_list[tables_count][1]=['production_genre_Robert_McKeey']
tables_list[tables_count][2]=['TEXT']
tables_list[tables_count][3]=tables_list[tables_count][1]
tables_list[tables_count][4]=[('爱情故事',),('恐怖影片',),('现代史诗',),('西部片',),('战争类型',),('成熟情节',),
                  			  ('赎罪情节',),('惩罚情节',),('考验情节',),('教育情节',),('幻灭情节',),('喜剧',),
			                  ('犯罪',),('社会剧',),('动作/冒险',),('历史剧',),('传记',),('纪实剧',),
			                  ('嘲讽纪录片',),('音乐片',),('科学幻想',),('体育类型',),('幻想',),('动画',),
			                  ('艺术电影',),('其他',)]
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1


#scope_production_genre_Blake_Snyder：Blake Snyder作品类型
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='scope_production_genre_Blake_Snyder'
tables_list[tables_count][1]=['production_genre_Blake_Snyder']
tables_list[tables_count][2]=['TEXT']
tables_list[tables_count][3]=tables_list[tables_count][1]
tables_list[tables_count][4]=[('金羊毛',),('爱情',),('超级英雄',),('鬼屋',),('侦探',),('如愿以偿',),
                  			  ('麻烦家伙',),('变迁仪式',),('愚者成功',),('被制度化',),('其他',)]
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1


#scope_production_MPAA_rating：作品美国电影分级
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='scope_production_MPAA_rating'
tables_list[tables_count][1]=['production_MPAA_rating']
tables_list[tables_count][2]=['TEXT']
tables_list[tables_count][3]=tables_list[tables_count][1]
tables_list[tables_count][4]=[('G',),('PG',),('PG-13',),('R',),('NC-17',),('X',)]
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1


# -------------------------以下为scene表字段限定范围-------------------------
#scope_scene_scenery：镜头景别
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='scope_scene_scenery'
tables_list[tables_count][1]=['scene_scenery_1','scene_scenery_2','scene_scenery_3']
tables_list[tables_count][2]=['TEXT','TEXT','TEXT']
tables_list[tables_count][3]=tables_list[tables_count][1]
tables_list[tables_count][4]=[('大炮的移动大全景','',''),('航拍的移动大全景','',''),
							  ('远景','正面全景',''),('远景','背面全景',''),('远景','侧面全景',''),('远景','俯视全景',''),('远景','仰拍全景',''),
							  ('中景','齐腹全景',''),('中景','齐胸全景',''),('中景','齐头全景',''),
							  ('特写','人物特写','眼部'),('特写','人物特写','手部'),('特写','人物特写','嘴部'),('特写','人物特写','身体局部'),
							  ('特写','物品特写',''),('特写','事件关注点特写',''),('特写','破坏性特写','')]
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1


#scope_scene_indoor_outdoor:镜头室内外
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='scope_scene_indoor_outdoor'
tables_list[tables_count][1]=['scene_indoor_outdoor']
tables_list[tables_count][2]=['TEXT']
tables_list[tables_count][3]=tables_list[tables_count][1]
tables_list[tables_count][4]=[('内景',),('外景',)]
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1


#scope_scene_time:镜头场景时间
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='scope_scene_time'
tables_list[tables_count][1]=['scene_time']
tables_list[tables_count][2]=['TEXT']
tables_list[tables_count][3]=tables_list[tables_count][1]
tables_list[tables_count][4]=[('日',),('夜',),('晨',),('黄昏',),('魔幻时刻',)]
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1


#scope_scene_subject_origin_place：镜头主体起始画面位置
#九宫格
#1-2-3
#4-5-6
#7-8-9
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='scope_scene_subject_origin_place'
tables_list[tables_count][1]=['scene_subject_origin_place']
tables_list[tables_count][2]=['TEXT']
tables_list[tables_count][3]=tables_list[tables_count][1]
tables_list[tables_count][4]=[('1宫',),('2宫',),('3宫',),('4宫',),('5宫',),('6宫',),('7宫',),('8宫',),('9宫',),
							  ('12线',),('23线',),('45线',),('56线',),('78线',),('89线',),
							  ('1245点',),('2356点',),('4578点',),('5689点',)]
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1


#scope_scene_subject_movement_trends：镜头主体起始画面位置
#九宫格左右上下移动格数量
#1-2-3
#4-5-6
#7-8-9
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='scope_scene_subject_movement_trends'
tables_list[tables_count][1]=['scene_subject_movement_trends']
tables_list[tables_count][2]=['TEXT']
tables_list[tables_count][3]=tables_list[tables_count][1]
tables_list[tables_count][4]=[('左0格上1格',),('左0格上2格',),('左0格上3格',),
							  ('左1格上0格',),('左1格上1格',),('左1格上2格',),('左1格上3格',),
							  ('左2格上0格',),('左2格上1格',),('左2格上2格',),('左2格上3格',),
							  ('左3格上0格',),('左3格上1格',),('左3格上2格',),('左3格上3格',),
							  ('左0格下1格',),('左0格下2格',),('左0格下3格',),
							  ('左1格下0格',),('左1格下1格',),('左1格下2格',),('左1格下3格',),
							  ('左2格下0格',),('左2格下1格',),('左2格下2格',),('左2格下3格',),
							  ('左3格下0格',),('左3格下1格',),('左3格下2格',),('左3格下3格',),
							  ('右0格上1格',),('右0格上2格',),('右0格上3格',),
							  ('右1格上0格',),('右1格上1格',),('右1格上2格',),('右1格上3格',),
							  ('右2格上0格',),('右2格上1格',),('右2格上2格',),('右2格上3格',),
							  ('右3格上0格',),('右3格上1格',),('右3格上2格',),('右3格上3格',),
							  ('右0格下1格',),('右0格下2格',),('右0格下3格',),
							  ('右1格下0格',),('右1格下1格',),('右1格下2格',),('右1格下3格',),
							  ('右2格下0格',),('右2格下1格',),('右2格下2格',),('右2格下3格',),
							  ('右3格下0格',),('右3格下1格',),('右3格下2格',),('右3格下3格',)
							  ]
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1


#scope_scene_place:镜头场景时间
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='scope_scene_place'
tables_list[tables_count][1]=['scene_place_1','scene_place_2','scene_place_3']
tables_list[tables_count][2]=['TEXT','TEXT','TEXT']
tables_list[tables_count][3]=tables_list[tables_count][1]
tables_list[tables_count][4]=[('内景','住所','多空间'),('内景','住所','客厅'),('内景','住所','卧室'),('内景','住所','厨房'),
							  ('内景','住所','卫生间'),('内景','住所','地下室'),('内景','住所','车库'),('内景','住所','杂物间'),
							  ('内景','住所','保姆间'),('内景','住所','浴室'),('内景','住所','楼道'),('内景','住所','门口'),
							  ('内景','住所','电梯'),('内景','住所','阁楼'),('内景','住所','其他'),
							  ('内景','办公','多空间'),('内景','办公','独立办公室'),('内景','办公','开放办公区'),
							  ('内景','办公','办公位'),('内景','办公','茶歇室'),('内景','办公','会议室'),('内景','办公','楼道'),
							  ('内景','办公','电梯'),('内景','办公','其他'),
							  ('内景','咖啡厅','多空间'),('内景','咖啡厅','大厅'),('内景','咖啡厅','吧台'),('内景','咖啡厅','卡座'),
							  ('内景','咖啡厅','洗手间'),('内景','咖啡厅','收银台'),('内景','咖啡厅','其他'),
							  ('内景','餐厅','多空间'),('内景','餐厅','大厅'),('内景','餐厅','包间'),('内景','餐厅','VIP房'),
							  ('内景','餐厅','洗手间'),('内景','餐厅','收银台'),('内景','餐厅','其他'),
							  ('内景','酒店','多空间'),('内景','酒店','卧室'),('内景','酒店','浴室'),('内景','酒店','卫生间'),
							  ('内景','酒店','走廊'),('内景','酒店','电梯'),('内景','酒店','其他'),
							  ('内景','医院','多空间'),('内景','医院','护士台'),('内景','医院','诊室'),('内景','医院','走廊'),
							  ('内景','医院','病房'),('内景','医院','收银台'),('内景','医院','更衣室'),('内景','医院','手术室'),
							  ('内景','医院','洗手间'),('内景','医院','其他'),
							  ('内景','商场/商店','多空间'),('内景','商场/商店','货架'),('内景','商场/商店','备货房'),
							  ('内景','商场/商店','门口'),('内景','商场/商店','收银台'),('内景','商场/商店','其他'),
							  ('内景','篮球馆','球场'),('内景','篮球馆','观众席'),('内景','篮球馆','更衣室'),('内景','篮球馆','其他'),
							  ('内景','羽毛球馆','球场'),('内景','羽毛球馆','观众席'),('内景','羽毛球馆','更衣室'),('内景','羽毛球馆','其他'),
							  ('内景','排球馆','球场'),('内景','排球馆','观众席'),('内景','排球馆','更衣室'),('内景','排球馆','其他'),
							  ('内景','乒乓球馆','球场'),('内景','乒乓球馆','观众席'),('内景','乒乓球馆','更衣室'),('内景','乒乓球馆','其他'),
							  ('内景','游泳馆','泳池'),('内景','游泳馆','跳台'),('内景','游泳馆','更衣室'),('内景','游泳馆','其他'),
							  ('内景','汽车','前排'),('内景','汽车','后排'),('内景','汽车','后备箱'),('内景','汽车','货车车厢'),('内景','汽车','其他'),
							  ('内景','火车','多空间'),('内景','火车','火车站候车室'),('内景','火车','火车站售票厅'),('内景','火车','驾驶室'),
							  ('内景','火车','车厢'),('内景','火车','洗手间'),('内景','火车','餐车'),('内景','火车','其他'),
							  ('内景','民用飞机','多空间'),('内景','民用飞机','机场安检处'),('内景','民用飞机','机场候机厅'),('内景','民用飞机','机场餐厅'),
							  ('内景','民用飞机','驾驶舱'),('内景','民用飞机','头等舱'),('内景','民用飞机','商务舱'),('内景','民用飞机','经济舱'),
							  ('内景','民用飞机','机组人员休息区'),('内景','民用飞机','洗手间'),('内景','民用飞机','行李舱'),('内景','民用飞机','其他'),
							  ('内景','军用飞机','多空间'),('内景','军用飞机','驾驶舱'),('内景','军用飞机','货物仓'),
							  ('内景','军用飞机','起落架仓'),('内景','军用飞机','弹药舱'),('内景','军用飞机','其他'),
							  ('内景','轮船','多空间'),('内景','轮船','驾驶室'),('内景','轮船','客房'),('内景','轮船','餐厅'),
							  ('内景','轮船','走廊'),('内景','轮船','动力室'),('内景','轮船','甲板'),('内景','轮船','其他'),
							  ('内景','地铁','多空间'),('内景','地铁','站台'),('内景','地铁','车厢'),('内景','地铁','驾驶舱'),
							  ('内景','地铁','隧道'),('内景','地铁','换乘通道'),('内景','地铁','其他'),
							  ('内景','洞穴','山洞'),('内景','洞穴','古墓'),('内景','洞穴','隧道'),('内景','洞穴','其他'),
							  ('内景','其他','其他'),
							  ('外景','城市','车行道'),('外景','城市','人行道'),('外景','城市','斑马线'),('外景','城市','城市中心区'),
							  ('外景','城市','远郊街道'),('外景','城市','居民区'),('外景','城市','商务区'),('外景','城市','公交车站'),
							  ('外景','城市','地铁站出入口'),('外景','城市','便利店门口'),('外景','城市','街角'),('外景','城市','小胡同'),
							  ('外景','城市','垃圾站'),('外景','城市','景区'),('外景','城市','广场'),('外景','城市','公园'),
							  ('外景','城市','别墅区'),('外景','城市','贫民窟'),('外景','城市','闹市区'),('外景','城市','其他'),
							  ('外景','乡村','田间小路'),('外景','乡村','农田'),('外景','乡村','乡村居住区'),('外景','乡村','院子'),
							  ('外景','乡村','其他'),
							  ('外景','铁路','铁轨'),('外景','铁路','隧道'),('外景','铁路','其他'),
							  ('外景','飞机场','停机坪'),('外景','飞机场','跑道'),('外景','飞机场','其他'),
							  ('外景','汽车站','停车场'),('外景','汽车站','其他'),
							  ('外景','河流','水面'),('外景','河流','水下'),('外景','河流','水岸'),('外景','河流','其他'),
							  ('外景','胡泊','水面'),('外景','胡泊','水下'),('外景','胡泊','水岸'),('外景','胡泊','其他'),
							  ('外景','海洋','水面'),('外景','海洋','水下'),('外景','海洋','沙滩'),('外景','海洋','礁石'),
							  ('外景','海洋','岛屿'),('外景','海洋','其他'),
							  ('外景','沙漠','沙漠'),('外景','沙漠','戈壁'),('外景','沙漠','绿洲'),('外景','沙漠','其他'),
							  ('外景','山脉','山顶'),('外景','山脉','山脚'),('外景','山脉','山腰'),('外景','山脉','雪山'),
							  ('外景','山脉','火山'),('外景','山脉','其他'),
							  ('外景','森林','森林'),('外景','草原','草原'),('外景','天空','天空'),
							  ('外景','宇宙','近地轨道'),('外景','宇宙','行星轨道'),('外景','宇宙','恒星轨道'),('外景','宇宙','星系外'),
							  ('外景','宇宙','特殊天体'),('外景','宇宙','其他'),
							  ('其他','其他','其他'),
							  ]
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1