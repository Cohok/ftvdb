# ====================================================================
# db_tables���������ݿ�����Ŀձ���Ϣ����Ϊ������Ϣ
# ���ߣ�huangpengjie����ϵ���䣺380781528@qq.com
# ====================================================================
tables_count = 0
tables_dict  = {}
tables_list  = []

#���һ�ű����Ϣ��ʹ������һ�������Ĵ���
# tables_list.append(['',[],[],[],[]])
# tables_list[tables_count][0]='table_name'
# tables_list[tables_count][1]=['*_id_last','column1']
# tables_list[tables_count][2]=['TEXT']
# tables_list[tables_count][3]=tables_list[tables_count][1][0]
# tables_list[tables_count][4]=[(0000,)]
# tables_dict[tables_count]=tables_list[tables_count][0]
# tables_count += 1


# ���TABLE participant��Ա��
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='participant'
tables_list[tables_count][1]=['participant_id_last',					# ���ڲ�ѯ��λparticipant_id���µ�����ֵ+1
							  'participant_id',							# 64λ������Ψһʶ����룬��0x��ͷ16λʮ�����Ʊ�ʾ�����ı���ʽ�洢���ڶ�ȡʱ��pythonת������
							  'participant_name',						# ��Ա����
							  'participant_stage_name',					# ��Ƶ����
							  'participant_other_call_1',				# ��Ա�����ƺ���ʽ1
							  'participant_other_call_2',				# ��Ա�����ƺ���ʽ2
							  'participant_other_call_3',				# ��Ա�����ƺ���ʽ3
							  'participant_other_call_4',				# ��Ա�����ƺ���ʽ4
							  'participant_other_call_5',				# ��Ա�����ƺ���ʽ5
							  'participant_gender',						# ��Ա�Ա�
							  'participant_intro_link',					# ��Ա��������
							  'PRIMARY KEY(participant_id)'															## ��������
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
							  ''																					## ��������
							  ]
tables_list[tables_count][3]=[tables_list[tables_count][1][0],tables_list[tables_count][1][1]]
tables_list[tables_count][4]=[('0x0000000000000000','0xffffffffffffffff')]	# ��ʼ��ʱ��production_id_last��λ��Ϊ1��ÿ����һ����¼������1
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1


# ���TABLE prole��ɫ��
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='proles'
tables_list[tables_count][1]=['proles_id_last',							# ���ڲ�ѯ��λparticipant_id���µ�����ֵ+1
							  'proles_id',								# 64λ������Ψһʶ����룬��0x��ͷ16λʮ�����Ʊ�ʾ�����ı���ʽ�洢���ڶ�ȡʱ��pythonת������
							  'proles_name',							# ���ν�ɫ����
							  'PRIMARY KEY(proles_id)'															## ��������
							  ]
tables_list[tables_count][2]=['TEXT',									# 'proles_id_last'
							  'TEXT NOT NULL UNIQUE',					# 'proles_id'
							  'TEXT',									# 'proles_name'
							  ''																					## ��������
							  ]
tables_list[tables_count][3]=[tables_list[tables_count][1][0],tables_list[tables_count][1][1]]
tables_list[tables_count][4]=[('0x0000000000000000','0xffffffffffffffff')]	# ��ʼ��ʱ��production_id_last��λ��Ϊ1��ÿ����һ����¼������1
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1


#���TABLE productions��Ʒ��
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='productions'
tables_list[tables_count][1]=['production_id_next',						# ���ڲ�ѯ��λproduction_id���µ�����ֵ+1
							  'production_id', 							# 64λ������Ψһʶ����룬��0x��ͷ16λʮ�����Ʊ�ʾ�����ı���ʽ�洢���ڶ�ȡʱ��pythonת������
							  'production_category',					# ��Ʒ���࣬������ƣ����Ʊ���Դ��TABLE scope_production_category
							  'production_name',						# ��Ʒ����
							  'production_other_name_1',				# ��Ʒ����1
							  'production_other_name_2',				# ��Ʒ����2
							  'production_other_name_3',				# ��Ʒ����3
							  'production_other_name_4',				# ��Ʒ����4
							  'production_other_name_5',				# ��Ʒ����5
							  'production_total_esipodes',				# ��Ʒ�ܼ���
							  'production_total_duration',				# ��Ʒ��ʱ������λΪ�룬��С����ʾ
							  'production_total_frames',				# ��Ʒ��֡��
							  'production_filming_time',				# ��Ʒ����ʱ�䣬����ܾ�ȷ����ʱ�䣬��ʱ���ʾ����������������������������
							  'production_release_time',				# ��Ʒ��ӳ�����У�ʱ�䣬����ָ���Ӿ磬��Ӱ���Բ���
							  'production_box_office',					# ��ƷƱ�����룬����ָ��Ӱ�����Ӿ���Բ���
							  'production_box_office_measurement',		# ��ƷƱ�����������λ��д�����Һ͵�λ
							  'production_release_income',				# ��Ʒ�������룬����ָ���Ӿ磬��Ӱ���Բ���
							  'production_release_income_measurement',	# ��Ʒ�������������λ, д�����Һ͵�λ
							  'production_background_time',				# ��Ʒ���±���ʱ��
							  'production_background_place',			# ��Ʒ���±����ص�
							  'production_novel_based',					# ��Ʒ�Ƿ����С˵�ı࣬1��ʾ�ǣ�0��ʾ��
							  'production_color',						# ��Ʒ�Ƿ��ɫ��1��ʾ��ɫ��0��ʾ�ڰ�
							  'production_plot_outline',				# ��Ʒ��ڵ�һ�仰�ܽ�
							  'production_plot_summary',				# ��Ʒ��ڼ��
							  'production_plot_keywords',				# ��Ʒ��ڹؼ���
							  'production_genre_Robert_McKee',			# ��Ʒ�޲���������ͣ��������TABLE scope_production_genre_Robert_McKee
							  'production_genre_Blake_Snyder',			# ��ƷBlake Snyder���ͣ��������TABLE scope_production_genre_Blake_Snyder
							  'production_MPAA_rating',					# ��Ʒ�����ĵ�Ӱ�ּ����������TALBE scope_production_MPAA_rating
							  'production_IMDb_average_user_rating',	# ��ƷIMDb����
							  'production_douban_average_user_rating',	# ��Ʒ��������
							  'production_link_to_official_site',		# ��Ʒ��������
							  'production_producers',					# ��Ʒ��Ƭ��
							  'production_dstributors',					# ��Ʒ������
							  'production_participant_1_id',			# ��Ʒ������1��id�������������Ӱ����Ա��Ϣ��TABLE participant�е�id
							  'production_participant_1_role',			# ��Ʒ������1�Ľ�ɫ�������������Ӱ����Ա��Ϣ��TABLE prole�еĽ�ɫ����id
							  'PRIMARY KEY(production_id)',															## ��������
							  'FOREIGN KEY(production_category)',													## �������production_category
							  'FOREIGN KEY(production_genre_Robert_McKee)',											## �������production_genre_Robert_McKee
							  'FOREIGN KEY(production_genre_Blake_Snyder)',											## �������production_genre_Robert_McKee
							  'FOREIGN KEY(production_MPAA_rating)'													## �������production_MPAA_rating
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
							  '',																					## ��������
							  'REFERENCES scope_production_category(production_category)',							## �����������production_category
							  'REFERENCES scope_production_genre_Robert_McKee(production_genre_Robert_McKee)',		## �����������production_genre_Robert_McKee
							  'REFERENCES scope_production_genre_Blake_Snyder(production_genre_Blake_Snyder)',		## �����������production_genre_Blake_Snyder
							  'REFERENCES scope_production_MPAA_rating(production_MPAA_rating)'						## �����������production_MPAA_rating
							  ]
tables_list[tables_count][3]=[tables_list[tables_count][1][0],tables_list[tables_count][1][1]]
tables_list[tables_count][4]=[('0x0000000000000000','0xffffffffffffffff')]	# ��ʼ��ʱ��production_id_last��λ��Ϊ1��ÿ����һ����¼������1
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1


#���TABLE videos��Ʒ������ֶ���Ϣ������ffmpeg�ɼ�����Ϣ
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='videos'
tables_list[tables_count][1]=[	'video_id_part',						# ���ڲ�ѯ��λvideo_id��video part����ֵ��32λ������Ψһʶ����룬��0x��ͷ8λʮ�����Ʊ�ʾ�����ı���ʽ�洢
								'video_id',								# video_id����video_id_partǰ������production_id��ÿ����Ƶ�еľ�ͷ��0��ʼ����
								'production_id',						# ��Ƶ������Ʒ��productions���е�production_id���������
								'video_episode',						# ��Ƶ�����������ڼ���
								'video_version',						# ��Ƶ�汾����Ϊһ����Ʒ���ܴ��ڶ���汾����Ƶ����ɾ���桢������ȣ��ڸ��ֶα�ע��Ψһ�汾��ע�����ע��v1��
								'video_db_file_basename',				# ��Ƶ�ļ���
								'video_db_file_extensionname',			# ��Ƶ�ļ���չ��
								'video_db_file_dir',					# ��Ƶ�����ļ���·��
								'video_db_file_path',					# ��Ƶ����·��
								#------------�����ֶ�Ϊffmpeg.probe['format']�ṩ���ֶ���Ϣ------------
								'video_probe',							# ffprobe�ַ����������Ϣ
								'video_filename',						# ��Ƶ�ļ�����·��������
								'video_db_name',						# ��Ƶ�ļ�basename
								'video_nb_streams',						# ��Ƶ��װ������
								'video_nb_programs',
								'video_format_name',
								'video_format_long_name',
								'video_start_time',
								'video_duration',
								'video_size',
								'video_bit_rate',
								'video_probe_score',
								'video_tags',
								#------------�����ֶ�Ϊffmpeg.probe['streams']����Ƶ���ṩ���ֶ���Ϣ------------
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
								#------------�����ֶ�Ϊffmpeg.probe['streams']��ƵƵ���ṩ���ֶ���Ϣ------------
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
								#------------�����ֶ�Ϊffmpeg.probe['streams']��ĻƵ���е�һ����Ļ���ṩ���ֶ���Ϣ------------
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
								#------------���²����ֶΣ��������������������Ϣ------------
							  	'PRIMARY KEY(video_id)',																## ��������
							  	'FOREIGN KEY(production_id)'															## �������production_id
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
								#------------�����ֶ�Ϊffmpeg.probe['format']�ṩ���ֶ���Ϣ------------
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
								#------------�����ֶ�Ϊffmpeg.probe['streams']����Ƶ���ṩ���ֶ���Ϣ------------
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
								#------------�����ֶ�Ϊffmpeg.probe['streams']��ƵƵ���ṩ���ֶ���Ϣ------------
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
								#------------�����ֶ�Ϊffmpeg.probe['streams']��ĻƵ���е�һ����Ļ���ṩ���ֶ���Ϣ------------
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
								#------------���²����ֶΣ��������������������Ϣ------------
							  	'',																					## ��������
							  	'REFERENCES productions(production_id)'												## �����������production_id
							  ]
tables_list[tables_count][3]=[]
tables_list[tables_count][4]=[]	# ��ʼ��ʱ��production_id_last��λ��Ϊ1��ÿ����һ����¼������1
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1

# ���TABLE scenes��ͷ��
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='scenes'
tables_list[tables_count][1]=['scene_id_part',							# ���ڲ�ѯ��λscene_id�е�scene part,����
							  'scene_id',								# scene_id����scene_id_partǰ������video_id��ÿ����ͷ��0��ʼ
							  'video_id', 								# ��ͷ������Ƶ��video_id������Ƶ
							  'production_id',							# ��ͷ������Ƶ������Ʒ��productions���е�production_id���������
							  'scene_in_point',							# ��ͷ��㣬��λΪ�룬�Ǵ���Ƶ��ʼ�ĵ�0������㿪ʼ��ʱ�����
							  'scene_out_point',						# ��ͷ���㣬��λΪ�룬�Ǵ���Ƶ��ʼ�ĵ�0�������������ʱ�����
							  'scene_duration',							# ��ͷ��ʱ��
							  'scene_in_point_frame',					# ��ͷ���֡��������ʹ����Ƶ�ĵڼ�֡
							  'scene_out_point_frame',					# ��ͷ����֡��������ʹ����Ƶ�ĵڼ�֡
							  'scene_file_basename',					# ��ͷ�ļ���
							  'scene_file_extensionname',				# ��ͷ�ļ���չ��
							  'scene_file_dir',							# ��ͷ�ļ�����Ŀ¼·��
							  'scene_file_path',						# ��ͷ�����ļ�·��
							  'scene_scenery_1',						# ��ͷ����1����������ƣ�����TABLE scope_scene_scenery
							  'scene_scenery_2',						# ��ͷ����2����������ƣ�����TABLE scope_scene_scenery
							  'scene_scenery_3',						# ��ͷ����3����������ƣ�����TABLE scope_scene_scenery
							  'scene_camera_position_height',			# ��ͷ��λ�߶�
							  'scene_indoor_outdoor',					# ��ͷ�ھ����⾰��������ƣ�����TABLE scope_scene_indoor_outdoor
							  'scene_place_2',							# ��ͷ�����ص�2����������ƣ�����TABLE scope_scene_place
							  'scene_place_3',							# ��ͷ�����ص�3����������ƣ�����TABLE scope_scene_place
							  'scene_time',								# ��ͷ����ʱ�䣬������ƣ�����TABLE scope_scene_time
							  'scene_subjects',							# ��ͷ����
							  'scene_accompany',						# ��ͷ����
							  'scene_subject_origin_place',				# ��ͷ������ʼλ�ã�������ƣ�����TABLE scope_scene_subject_origin_place
							  'scene_subject_movement_trends',			# ��ͷ���嶯�Ʒ���������ƣ�����TABLE scope_scene_subject_movement_trends
							  'scene_focus_lens',						# ��ͷ����
							  'scene_foreground_content',				# ��ͷǰ������
							  'scene_background_content',				# ��ͷǰ������
							  'scene_camera_movemet',					# ��ͷ�ƶ�����
							  'PRIMARY KEY(scene_id)',																## ��������
							  'FOREIGN KEY(production_id)',															## �������production_id
							  'FOREIGN KEY(video_id)',																## �������video_id
							  'FOREIGN KEY(scene_scenery_1)',														## �������scene_scenery_1
							  'FOREIGN KEY(scene_scenery_2)',														## �������scene_scenery_2
							  'FOREIGN KEY(scene_scenery_3)',														## �������scene_scenery_3
							  'FOREIGN KEY(scene_indoor_outdoor)',													## �������scene_indoor_outdoor
							  'FOREIGN KEY(scene_place_2)',															## �������scene_place_2
							  'FOREIGN KEY(scene_place_3)',															## �������scene_place_3
							  'FOREIGN KEY(scene_time)',															## �������scene_time
							  'FOREIGN KEY(scene_subject_origin_place)',											## �������subject_origin_place
							  'FOREIGN KEY(scene_subject_movement_trends)'											## �������subject_movement_trends
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
							  '',																					## ��������
							  'REFERENCES productions(production_id)',												## �����������production_id
							  'REFERENCES videos(video_id)',														## �����������video_id
							  'REFERENCES scope_scene_scenery(scene_scenery_1)',									## �����������scene_scenery_1
							  'REFERENCES scope_scene_scenery(scene_scenery_2)',									## �����������scene_scenery_2
							  'REFERENCES scope_scene_scenery(scene_scenery_3)',									## �����������scene_scenery_3
							  'REFERENCES scope_scene_indoor_outdoor(scene_indoor_outdoor)',						## �����������scene_scenery_3
							  'REFERENCES scope_scene_place(scene_place_2)',										## �����������scene_place_2
							  'REFERENCES scope_scene_place(scene_place_3)',										## �����������scene_place_3
							  'REFERENCES scope_scene_time(scene_time)',											## �����������scene_time
							  'REFERENCES scope_scene_subject_origin_place(scene_subject_origin_place)',			## �����������scene_subject_origin_place
							  'REFERENCES scope_scene_subject_movement_trends(scene_subject_movement_trends)'		## �����������scene_subject_movement_trends
							  ]
tables_list[tables_count][3]=[]
tables_list[tables_count][4]=[]	# ��ʼ��ʱ��production_id_last��λ��Ϊ1��ÿ����һ����¼������1
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1

#���TABLE frames֡��
tables_list.append(['',[],[],[],[]])
tables_list[tables_count][0]='frames'
tables_list[tables_count][1]=['frame_id_part',							# ���ڲ�ѯ��λscene_id�е�scene part,
							  'frame_id',								# frame_id��scene_id + frame_id_part
							  'scene_id',								# scene_id����scene_id_partǰ������video_id��ÿ����ͷ��0��ʼ
							  'video_id', 								# ��ͷ������Ƶ��video_id������Ƶ
							  'production_id',							# ��ͷ������Ƶ������Ʒ��productions���е�production_id���������
							  'frame_timecode',							# ֡ʱ��
							  'frame_sequence_nb',						# ֡����
							  'frame_file_basename',					# ֡�ļ���
							  'frame_file_extensionname',				# ֡�ļ���չ��
							  'frame_file_dir',							# ֡�ļ�����Ŀ¼·��
							  'frame_file_path',						# ֡�ļ�����·��
							  'PRIMARY KEY(frame_id)',																## ��������
							  'FOREIGN KEY(scene_id)',																## �������production_id
							  'FOREIGN KEY(production_id)',															## �������production_id
							  'FOREIGN KEY(video_id)',																## �������video_id
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
							  '',																					## ��������
							  'REFERENCES scenes(scene_id)',														## �����������production_id
							  'REFERENCES productions(production_id)',												## �����������production_id
							  'REFERENCES videos(video_id)',														## �����������video_id
							  ]
tables_list[tables_count][3]=[]
tables_list[tables_count][4]=[]	# ��ʼ��ʱ��production_id_last��λ��Ϊ1��ÿ����һ����¼������1
tables_dict[tables_count]=tables_list[tables_count][0]
tables_count += 1