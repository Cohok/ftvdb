# ====================================================================
# db_tables包含了数据库主表的空表信息，作为常数信息
# 作者：huangpengjie，联系邮箱：380781528@qq.com
# ====================================================================
tables_count = 0
tables_dict  = {}
tables_list  = []

#添加一张表的信息就使用下面一段完整的代码
# tables_list.append(['',[],[],[],[]])
# tables_list[tables_count][0]='table_name'
# tables_list[tables_count][1]=['*_id_last','column1']
# tables_list[tables_count][2]=['TEXT']
# tables_list[tables_count][3]=tables_list[tables_count][1][0]
# tables_list[tables_count][4]=[(0000,)]
# tables_dict[tables_count]=tables_list[tables_count][0]
# tables_count += 1


# 添加TABLE participant人员表
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='participant'
tables_list[tables_count][1]=['participant_id_last',					# 用于查询定位participant_id更新的最新值+1
							  'participant_id',							# 64位二进制唯一识别编码，以0x开头16位十六进制表示，以文本形式存储，在读取时用python转换计算
							  'participant_name',						# 人员姓名
							  'participant_stage_name',					# 视频艺名
							  'participant_other_call_1',				# 人员其他称呼方式1
							  'participant_other_call_2',				# 人员其他称呼方式2
							  'participant_other_call_3',				# 人员其他称呼方式3
							  'participant_other_call_4',				# 人员其他称呼方式4
							  'participant_other_call_5',				# 人员其他称呼方式5
							  'participant_gender',						# 人员性别
							  'participant_intro_link',					# 人员介绍链接
							  'PRIMARY KEY(participant_id)'															## 设置主键
							  ]
tables_list[tables_count][2]=['TEXT',									# 'participant_id_last'
							  'TEXT NOT NULL UNIQUE',					# 'participant_id'
							  'TEXT',									# 'participant_name'
							  'TEXT',									# 'participant_stage_name'
							  'TEXT',									# 'participant_other_call_1'
							  'TEXT',									# 'participant_other_call_2'
							  'TEXT',									# 'participant_other_call_3'
							  'TEXT',									# 'participant_other_call_4'
							  'TEXT',									# 'participant_other_call_5'
							  'TEXT',									# 'participant_gender'
							  'TEXT',									# 'participant_intro_link'
							  ''																					## 设置主键
							  ]
tables_list[tables_count][3]=[tables_list[tables_count][1][0],tables_list[tables_count][1][1]]
tables_list[tables_count][4]=[('0x0000000000000000','0xffffffffffffffff')]	# 初始化时，production_id_last定位数为1，每增加一条记录，增加1
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1


# 添加TABLE prole角色表
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='proles'
tables_list[tables_count][1]=['proles_id_last',							# 用于查询定位participant_id更新的最新值+1
							  'proles_id',								# 64位二进制唯一识别编码，以0x开头16位十六进制表示，以文本形式存储，在读取时用python转换计算
							  'proles_name',							# 担任角色名称
							  'PRIMARY KEY(proles_id)'															## 设置主键
							  ]
tables_list[tables_count][2]=['TEXT',									# 'proles_id_last'
							  'TEXT NOT NULL UNIQUE',					# 'proles_id'
							  'TEXT',									# 'proles_name'
							  ''																					## 设置主键
							  ]
tables_list[tables_count][3]=[tables_list[tables_count][1][0],tables_list[tables_count][1][1]]
tables_list[tables_count][4]=[('0x0000000000000000','0xffffffffffffffff')]	# 初始化时，production_id_last定位数为1，每增加一条记录，增加1
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1


#添加TABLE productions作品表
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='productions'
tables_list[tables_count][1]=['production_id_next',						# 用于查询定位production_id更新的最新值+1
							  'production_id', 							# 64位二进制唯一识别编码，以0x开头16位十六进制表示，以文本形式存储，在读取时用python转换计算
							  'production_category',					# 作品分类，外键限制，限制表来源于TABLE scope_production_category
							  'production_name',						# 作品名称
							  'production_other_name_1',				# 作品别名1
							  'production_other_name_2',				# 作品别名2
							  'production_other_name_3',				# 作品别名3
							  'production_other_name_4',				# 作品别名4
							  'production_other_name_5',				# 作品别名5
							  'production_total_esipodes',				# 作品总集数
							  'production_total_duration',				# 作品总时长，单位为秒，用小数表示
							  'production_total_frames',				# 作品总帧数
							  'production_filming_time',				# 作品拍摄时间，如果能精确描述时间，用时间表示，否则用文字描述，如年代、年份
							  'production_release_time',				# 作品播映（发行）时间，这里指电视剧，电影可以不填
							  'production_box_office',					# 作品票房收入，这里指电影，电视剧可以不填
							  'production_box_office_measurement',		# 作品票房收入计量单位，写明货币和单位
							  'production_release_income',				# 作品发行收入，这里指电视剧，电影可以不填
							  'production_release_income_measurement',	# 作品发行收入计量单位, 写明货币和单位
							  'production_background_time',				# 作品故事背景时间
							  'production_background_place',			# 作品故事背景地点
							  'production_novel_based',					# 作品是否基于小说改编，1表示是，0表示否
							  'production_color',						# 作品是否彩色，1表示彩色，0表示黑白
							  'production_plot_outline',				# 作品情节的一句话总结
							  'production_plot_summary',				# 作品情节简介
							  'production_plot_keywords',				# 作品情节关键词
							  'production_genre_Robert_McKee',			# 作品罗伯特麦基类型，来自外键TABLE scope_production_genre_Robert_McKee
							  'production_genre_Blake_Snyder',			# 作品Blake Snyder类型，来自外键TABLE scope_production_genre_Blake_Snyder
							  'production_MPAA_rating',					# 作品美国的电影分级，来自外键TALBE scope_production_MPAA_rating
							  'production_IMDb_average_user_rating',	# 作品IMDb评分
							  'production_douban_average_user_rating',	# 作品豆瓣评分
							  'production_link_to_official_site',		# 作品官网链接
							  'production_producers',					# 作品制片人
							  'production_dstributors',					# 作品发行人
							  'production_participant_1_id',			# 作品参与人1的id，来自外键，在影视人员信息表TABLE participant中的id
							  'production_participant_1_role',			# 作品参与人1的角色，来自外键，在影视人员信息表TABLE prole中的角色分类id
							  'PRIMARY KEY(production_id)',															## 设置主键
							  'FOREIGN KEY(production_category)',													## 外键条件production_category
							  'FOREIGN KEY(production_genre_Robert_McKee)',											## 外键条件production_genre_Robert_McKee
							  'FOREIGN KEY(production_genre_Blake_Snyder)',											## 外键条件production_genre_Robert_McKee
							  'FOREIGN KEY(production_MPAA_rating)'													## 外键条件production_MPAA_rating
							  ]
tables_list[tables_count][2]=['TEXT',									# 'production_id_next'
							  'TEXT NOT NULL UNIQUE',					# 'production_id'
							  'TEXT',									# 'production_category'
							  'TEXT',									# 'production_name'
							  'TEXT',									# 'production_other_name_1'
							  'TEXT',									# 'production_other_name_2'
							  'TEXT',									# 'production_other_name_3'
							  'TEXT',									# 'production_other_name_4'
							  'TEXT',									# 'production_other_name_5'
							  'INTEGER',								# 'production_total_esipodes',
							  'REAL',									# 'production_total_running_time'
							  'INTEGER',								# 'production_total_frames'
							  'TEXT',									# 'production_filming_time'
							  'TEXT',									# 'production_release_time'
							  'REAL',									# 'production_box_office'
							  'TEXT',									# 'production_box_office_measurement'
							  'REAL',									# 'production_release_income'
							  'TEXT',									# 'production_box_office_measurement'
							  'TEXT',									# 'production_background_time'
							  'TEXT',									# 'production_background_place'
							  'BOOLEAN',								# 'production_novel_based',
							  'BOOLEAN',								# 'production_color'
							  'TEXT',									# 'production_plot_outline'	
							  'TEXT',									# 'production_plot_summary'
							  'TEXT',									# 'production_plot_keywords'
							  'TEXT',									# 'production_genre_Robert_McKee'
							  'TEXT',									# 'production_genre_Blake_Snyder'
							  'TEXT',									# 'roduction_MPAA_rating'
							  'REAL',									# 'production_IMDb_average_user_rating'
							  'REAL',									# 'production_douban_average_user_rating'
							  'TEXT',									# 'production_link_to_official_site'
							  'TEXT',									# 'production_producers'
							  'TEXT',									# 'production_dstributors'
							  'TEXT',									# 'production_participant_1_id'
							  'TEXT',									# 'production_participant_1_role'
							  '',																					## 设置主键
							  'REFERENCES scope_production_category(production_category)',							## 外键条件参照production_category
							  'REFERENCES scope_production_genre_Robert_McKee(production_genre_Robert_McKee)',		## 外键条件参照production_genre_Robert_McKee
							  'REFERENCES scope_production_genre_Blake_Snyder(production_genre_Blake_Snyder)',		## 外键条件参照production_genre_Blake_Snyder
							  'REFERENCES scope_production_MPAA_rating(production_MPAA_rating)'						## 外键条件参照production_MPAA_rating
							  ]
tables_list[tables_count][3]=[tables_list[tables_count][1][0],tables_list[tables_count][1][1]]
tables_list[tables_count][4]=[('0x0000000000000000','0xffffffffffffffff')]	# 初始化时，production_id_last定位数为1，每增加一条记录，增加1
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1


#添加TABLE videos作品表，表格字段信息均来自ffmpeg采集的信息
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='videos'
tables_list[tables_count][1]=[	'video_id_part',						# 用于查询定位video_id中video part的数值，32位二进制唯一识别编码，以0x开头8位十六进制表示，以文本形式存储
								'video_id',								# video_id是在video_id_part前面连接production_id，每个视频中的镜头从0开始排序
								'production_id',						# 视频所属作品在productions表中的production_id，外键限制
								'video_episode',						# 视频集序数，即第几集
								'video_version',						# 视频版本，因为一部作品可能存在多个版本的视频，如删减版、地区版等，在该字段标注，唯一版本标注建议标注“v1”
								'video_db_file_basename',				# 视频文件名
								'video_db_file_extensionname',			# 视频文件扩展名
								'video_db_file_dir',					# 视频所在文件夹路径
								'video_db_file_path',					# 视频完整路径
								#------------以下字段为ffmpeg.probe['format']提供的字段信息------------
								'video_probe',							# ffprobe字符串化后的信息
								'video_filename',						# 视频文件完整路径及名字
								'video_db_name',						# 视频文件basename
								'video_nb_streams',						# 视频封装流数量
								'video_nb_programs',
								'video_format_name',
								'video_format_long_name',
								'video_start_time',
								'video_duration',
								'video_size',
								'video_bit_rate',
								'video_probe_score',
								'video_tags',
								#------------以下字段为ffmpeg.probe['streams']中视频流提供的字段信息------------
								'video_v_index',
								'video_v_codec_name',
								'video_v_codec_long_name',
								'video_v_profile',
								'video_v_codec_type',
								'video_v_codec_tag_string',
								'video_v_codec_tag',
								'video_v_width',
								'video_v_height',
								'video_v_coded_width',
								'video_v_coded_height',
								'video_v_closed_captions',
								'video_v_film_grain',
								'video_v_has_b_frames',
								'video_v_sample_aspect_ratio',
								'video_v_display_aspect_ratio',
								'video_v_pix_fmt',
								'video_v_level',
								'video_v_color_range',
								'video_v_color_space',
								'video_v_color_transfer',
								'video_v_color_primaries',
								'video_v_chroma_location',
								'video_v_field_order',
								'video_v_refs',
								'video_v_is_avc',
								'video_v_nal_length_size',
								'video_v_r_frame_rate',
								'video_v_avg_frame_rate',
								'video_v_time_base',
								'video_v_start_pts',
								'video_v_start_time',
								'video_v_duration_ts',
								'video_v_duration',
								'video_v_bit_rate',
								'video_v_bits_per_raw_sample',
								'video_v_nb_frames',
								'video_v_extradata_size',
								'video_v_disposition',
								'video_v_tags',
								'video_v_id',
								#------------以下字段为ffmpeg.probe['streams']音频频流提供的字段信息------------
								'video_a_index',
								'video_a_codec_name',
								'video_a_codec_long_name',
								'video_a_profile',
								'video_a_codec_type',
								'video_a_codec_tag_string',
								'video_a_codec_tag',
								'video_a_sample_fmt',
								'video_a_sample_rate',
								'video_a_channels',
								'video_a_channel_layout',
								'video_a_bits_per_sample',
								'video_a_initial_padding',
								'video_a_r_frame_rate',
								'video_a_avg_frame_rate',
								'video_a_time_base',
								'video_a_start_pts',
								'video_a_start_time',
								'video_a_extradata_size',
								'video_a_disposition',
								'video_a_tags',
								#------------以下字段为ffmpeg.probe['streams']字幕频流中第一个字幕流提供的字段信息------------
								'video_s_index',
								'video_s_codec_name',
								'video_s_codec_long_name',
								'video_s_codec_type',
								'video_s_codec_tag_string',
								'video_s_codec_tag',
								'video_s_r_frame_rate',
								'video_s_avg_frame_rate',
								'video_s_time_base',
								'video_s_start_pts',
								'video_s_start_time',
								'video_s_duration_ts',
								'video_s_duration',
								'video_s_extradata_size',
								'video_s_disposition',
								'video_s_tags',
								#------------以下不是字段，是设置主键和外键的信息------------
							  	'PRIMARY KEY(video_id)',																## 设置主键
							  	'FOREIGN KEY(production_id)'															## 外键条件production_id
							  ]
tables_list[tables_count][2]=[	'TEXT',									# 'video_id_part'
							  	'TEXT NOT NULL UNIQUE',					# 'video_id'
							  	'TEXT',									# 'production_id'
							  	'TEXT',									# 'video_version'
							  	'INTEGER',								# 'video_episode'
							  	'TEXT',									# 'video_db_file_basename'
							  	'TEXT',									# 'video_db_file_extensionname'
							  	'TEXT',									# 'video_db_file_dir'
							  	'TEXT',									# 'video_db_file_path'
								#------------以下字段为ffmpeg.probe['format']提供的字段信息------------
								'TEXT',									# 'video_probe',
								'TEXT',									# 'video_filename',	
								'TEXT',									# 'video_db_name'					
								'INTEGER',								# 'video_nb_streams',						
								'INTEGER',								# 'video_nb_programs',
								'TEXT',									# 'video_format_name',
								'TEXT',									# 'video_format_long_name',
								'TEXT',									# 'video_start_time',
								'TEXT',									# 'video_duration',
								'TEXT',									# 'video_size',
								'TEXT',									# 'video_bit_rate',
								'INTEGER',								# 'video_probe_score',
								'TEXT',									# 'video_tags',
								#------------以下字段为ffmpeg.probe['streams']中视频流提供的字段信息------------
								'INTEGER',								# 'video_v_index',
								'TEXT',									# 'video_v_codec_name',
								'TEXT',									# 'video_v_codec_long_name',
								'TEXT',									# 'video_v_profile',
								'TEXT',									# 'video_v_codec_type',
								'TEXT',									# 'video_v_codec_tag_string',
								'TEXT',									# 'video_v_codec_tag',
								'INTEGER',								# 'video_v_width',
								'INTEGER',								# 'video_v_height',
								'INTEGER',								# 'video_v_coded_width',
								'INTEGER',								# 'video_v_coded_height',
								'INTEGER',								# 'video_v_closed_captions',
								'INTEGER',								# 'video_v_film_grain',
								'INTEGER',								# 'video_v_has_b_frames',
								'TEXT',									# 'video_v_sample_aspect_ratio',
								'TEXT',									# 'video_v_display_aspect_ratio',
								'TEXT',									# 'video_v_pix_fmt',
								'INTEGER',								# 'video_v_level',
								'TEXT',									# 'video_v_color_range',
								'TEXT',									# 'video_v_color_space',
								'TEXT',									# 'video_v_color_transfer',
								'TEXT',									# 'video_v_color_primaries',
								'TEXT',									# 'video_v_chroma_location',
								'TEXT',									# 'video_v_field_order',
								'INTEGER',								# 'video_v_refs',
								'TEXT',									# 'video_v_is_avc',
								'TEXT',									# 'video_v_nal_length_size',
								'TEXT',									# 'video_v_r_frame_rate',
								'TEXT',									# 'video_v_avg_frame_rate',
								'TEXT',									# 'video_v_time_base',
								'INTEGER',								# 'video_v_start_pts',
								'TEXT',									# 'video_v_start_time',
								'INTEGER',								# 'video_v_duration_ts',
								'TEXT',									# 'video_v_duration',
								'TEXT',									# 'video_v_bit_rate',
								'TEXT',									# 'video_v_bits_per_raw_sample',
								'TEXT',									# 'video_v_nb_frames',
								'INTEGER',								# 'video_v_extradata_size',
								'TEXT',									# 'video_v_disposition',
								'TEXT',									# 'video_v_tags',
								'TEXT',									# 'video_v_id',
								#------------以下字段为ffmpeg.probe['streams']音频频流提供的字段信息------------
								'INTEGER',								# 'video_a_index',
								'TEXT',									# 'video_a_codec_name',
								'TEXT',									# 'video_a_codec_long_name',
								'TEXT',									# 'video_a_profile',
								'TEXT',									# 'video_a_codec_type',
								'TEXT',									# 'video_a_codec_tag_string',
								'TEXT',									# 'video_a_codec_tag',
								'TEXT',									# 'video_a_sample_fmt',
								'TEXT',									# 'video_a_sample_rate',
								'INTEGER',								# 'video_a_channels',
								'TEXT',									# 'video_a_channel_layout',
								'INTEGER',								# 'video_a_bits_per_sample',
								'INTEGER',								# 'video_a_initial_padding',
								'TEXT',									# 'video_a_r_frame_rate',
								'TEXT',									# 'video_a_avg_frame_rate',
								'TEXT',									# 'video_a_time_base',
								'TEXT',									# 'video_a_start_pts',
								'TEXT',									# 'video_a_start_time',
								'INTEGER',								# 'video_a_extradata_size',
								'TEXT',									# 'video_a_disposition',
								'TEXT',									# 'video_a_tags',
								#------------以下字段为ffmpeg.probe['streams']字幕频流中第一个字幕流提供的字段信息------------
								'INTEGER',								# 'video_s_index',
								'TEXT',									# 'video_s_codec_name',
								'TEXT',									# 'video_s_codec_long_name',
								'TEXT',									# 'video_s_codec_type',
								'TEXT',									# 'video_s_codec_tag_string',
								'TEXT',									# 'video_s_codec_tag',
								'TEXT',									# 'video_s_r_frame_rate',
								'TEXT',									# 'video_s_avg_frame_rate',
								'TEXT',									# 'video_s_time_base',
								'TEXT',									# 'video_s_start_pts',
								'TEXT',									# 'video_s_start_time',
								'INTEGER',								# 'video_s_duration_ts',
								'TEXT',									# 'video_s_duration',								
								'INTEGER',								# 'video_s_extradata_size',
								'TEXT',									# 'video_s_disposition',
								'TEXT',									# 'video_s_tags',
								#------------以下不是字段，是设置主键和外键的信息------------
							  	'',																					## 设置主键
							  	'REFERENCES productions(production_id)'												## 外键条件参照production_id
							  ]
tables_list[tables_count][3]=[]
tables_list[tables_count][4]=[]	# 初始化时，production_id_last定位数为1，每增加一条记录，增加1
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1

# 添加TABLE scenes镜头表
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='scenes'
tables_list[tables_count][1]=['scene_id_part',							# 用于查询定位scene_id中的scene part,整数
							  'scene_id',								# scene_id是在scene_id_part前面连接video_id，每个镜头从0开始
							  'video_id', 								# 镜头所属视频的video_id，在视频
							  'production_id',							# 镜头所属视频所在作品在productions表中的production_id，外键限制
							  'scene_in_point',							# 镜头入点，单位为秒，是从视频开始的第0秒至入点开始的时间距离
							  'scene_out_point',						# 镜头出点，单位为秒，是从视频开始的第0秒至出点结束的时间距离
							  'scene_duration',							# 镜头总时长
							  'scene_in_point_frame',					# 镜头入点帧序数，即使在视频的第几帧
							  'scene_out_point_frame',					# 镜头出点帧序数，即使在视频的第几帧
							  'scene_file_basename',					# 镜头文件名
							  'scene_file_extensionname',				# 镜头文件扩展名
							  'scene_file_dir',							# 镜头文件所在目录路径
							  'scene_file_path',						# 镜头完整文件路径
							  'scene_scenery_1',						# 镜头景别1级，外键限制，来自TABLE scope_scene_scenery
							  'scene_scenery_2',						# 镜头景别2级，外键限制，来自TABLE scope_scene_scenery
							  'scene_scenery_3',						# 镜头景别3级，外键限制，来自TABLE scope_scene_scenery
							  'scene_camera_position_height',			# 镜头机位高度
							  'scene_indoor_outdoor',					# 镜头内景、外景，外键限制，来自TABLE scope_scene_indoor_outdoor
							  'scene_place_2',							# 镜头场景地点2级，外键限制，来自TABLE scope_scene_place
							  'scene_place_3',							# 镜头场景地点3级，外键限制，来自TABLE scope_scene_place
							  'scene_time',								# 镜头场景时间，外键限制，来自TABLE scope_scene_time
							  'scene_subjects',							# 镜头主体
							  'scene_accompany',						# 镜头陪体
							  'scene_subject_origin_place',				# 镜头主体起始位置，外键限制，来自TABLE scope_scene_subject_origin_place
							  'scene_subject_movement_trends',			# 镜头主体动势方向，外键限制，来自TABLE scope_scene_subject_movement_trends
							  'scene_focus_lens',						# 镜头焦距
							  'scene_foreground_content',				# 镜头前景内容
							  'scene_background_content',				# 镜头前景内容
							  'scene_camera_movemet',					# 镜头移动方法
							  'PRIMARY KEY(scene_id)',																## 设置主键
							  'FOREIGN KEY(production_id)',															## 外键条件production_id
							  'FOREIGN KEY(video_id)',																## 外键条件video_id
							  'FOREIGN KEY(scene_scenery_1)',														## 外键条件scene_scenery_1
							  'FOREIGN KEY(scene_scenery_2)',														## 外键条件scene_scenery_2
							  'FOREIGN KEY(scene_scenery_3)',														## 外键条件scene_scenery_3
							  'FOREIGN KEY(scene_indoor_outdoor)',													## 外键条件scene_indoor_outdoor
							  'FOREIGN KEY(scene_place_2)',															## 外键条件scene_place_2
							  'FOREIGN KEY(scene_place_3)',															## 外键条件scene_place_3
							  'FOREIGN KEY(scene_time)',															## 外键条件scene_time
							  'FOREIGN KEY(scene_subject_origin_place)',											## 外键条件subject_origin_place
							  'FOREIGN KEY(scene_subject_movement_trends)'											## 外键条件subject_movement_trends
							  ]
tables_list[tables_count][2]=['INTEGER',								# 'scene_id_part'
							  'TEXT NOT NULL UNIQUE',					# 'scene_id'
							  'TEXT',									# 'video_id'
							  'TEXT',									# 'production_id'
							  'REAL',									# 'scene_in_point'
							  'REAL',									# 'scene_out_point'
							  'REAL',									# 'scene_duration'
							  'INTEGER',								# 'scene_in_point_frame'
							  'INTEGER',								# 'scene_out_point_frame'
							  'TEXT',									# 'scene_file_basename'
							  'TEXT',									# 'scene_file_extensionname'
							  'TEXT',									# 'scene_file_dir'
							  'TEXT',									# 'scene_file_path'
							  'TEXT',									# 'scene_scenery_1'
							  'TEXT',									# 'scene_scenery_2'
							  'TEXT',									# 'scene_scenery_3'
							  'TEXT',									# 'scene_camera_position_height'
							  'TEXT',									# 'scene_indoor_outdoor'
							  'TEXT',									# 'scene_place_2'
							  'TEXT',									# 'scene_place_3'
							  'TEXT',									# 'scene_time'
							  'TEXT',									# 'scene_subjects'
							  'TEXT',									# 'scene_accompany'
							  'TEXT',									# 'scene_subject_origin_place'
							  'TEXT',									# 'scene_subject_movement_trends'
							  'TEXT',									# 'scene_focus_lens'
							  'TEXT',									# 'scene_foreground_content'
							  'TEXT',									# 'scene_background_content'
							  'TEXT',									# 'scene_camera_movemet'
							  '',																					## 设置主键
							  'REFERENCES productions(production_id)',												## 外键条件参照production_id
							  'REFERENCES videos(video_id)',														## 外键条件参照video_id
							  'REFERENCES scope_scene_scenery(scene_scenery_1)',									## 外键条件参照scene_scenery_1
							  'REFERENCES scope_scene_scenery(scene_scenery_2)',									## 外键条件参照scene_scenery_2
							  'REFERENCES scope_scene_scenery(scene_scenery_3)',									## 外键条件参照scene_scenery_3
							  'REFERENCES scope_scene_indoor_outdoor(scene_indoor_outdoor)',						## 外键条件参照scene_scenery_3
							  'REFERENCES scope_scene_place(scene_place_2)',										## 外键条件参照scene_place_2
							  'REFERENCES scope_scene_place(scene_place_3)',										## 外键条件参照scene_place_3
							  'REFERENCES scope_scene_time(scene_time)',											## 外键条件参照scene_time
							  'REFERENCES scope_scene_subject_origin_place(scene_subject_origin_place)',			## 外键条件参照scene_subject_origin_place
							  'REFERENCES scope_scene_subject_movement_trends(scene_subject_movement_trends)'		## 外键条件参照scene_subject_movement_trends
							  ]
tables_list[tables_count][3]=[]
tables_list[tables_count][4]=[]	# 初始化时，production_id_last定位数为1，每增加一条记录，增加1
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1

#添加TABLE frames帧表
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='frames'
tables_list[tables_count][1]=['frame_id_part',							# 用于查询定位scene_id中的scene part,
							  'frame_id',								# frame_id是scene_id + frame_id_part
							  'scene_id',								# scene_id是在scene_id_part前面连接video_id，每个镜头从0开始
							  'video_id', 								# 镜头所属视频的video_id，在视频
							  'production_id',							# 镜头所属视频所在作品在productions表中的production_id，外键限制
							  'frame_timecode',							# 帧时刻
							  'frame_sequence_nb',						# 帧序数
							  'frame_file_basename',					# 帧文件名
							  'frame_file_extensionname',				# 帧文件扩展名
							  'frame_file_dir',							# 帧文件所在目录路径
							  'frame_file_path',						# 帧文件完整路径
							  'PRIMARY KEY(frame_id)',																## 设置主键
							  'FOREIGN KEY(scene_id)',																## 外键条件production_id
							  'FOREIGN KEY(production_id)',															## 外键条件production_id
							  'FOREIGN KEY(video_id)',																## 外键条件video_id
							  ]
tables_list[tables_count][2]=['INTEGER',								# 'frame_id_part'
							  'TEXT NOT NULL UNIQUE',					# 'frame_id'
							  'TEXT ',									# 'scene_id'
							  'TEXT',									# 'video_id'
							  'TEXT',									# 'production_id'
							  'TEXT',									# 'frame_timecode'
							  'INTEGER',								# 'frame_sequence_nb'
							  'TEXT',									# 'frame_file_basename',
							  'TEXT',									# 'frame_file_extensionname',
							  'TEXT',									# 'frame_file_dir'
							  'TEXT',									# 'frame_file_path'
							  '',																					## 设置主键
							  'REFERENCES scenes(scene_id)',														## 外键条件参照production_id
							  'REFERENCES productions(production_id)',												## 外键条件参照production_id
							  'REFERENCES videos(video_id)',														## 外键条件参照video_id
							  ]
tables_list[tables_count][3]=[]
tables_list[tables_count][4]=[]	# 初始化时，production_id_last定位数为1，每增加一条记录，增加1
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1