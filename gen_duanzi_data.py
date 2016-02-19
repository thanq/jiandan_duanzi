# -*- coding:utf-8 -*-

from util.fileutil import get_all_duanzi_dict_list
from util.jsonutil import dict_to_json
from datacenter.duanzi_gen_service import add_duanzi_json_to_all_duanzi_json_data, \
    add_duanzi_zan_floor_redis_sort_set, gen_top_rank_duanzi_floor_list, \
    rename_top_list_name_for_web


for duanzi_dict in get_all_duanzi_dict_list():
    add_duanzi_json_to_all_duanzi_json_data(duanzi_dict['floor'], dict_to_json(duanzi_dict))
    add_duanzi_zan_floor_redis_sort_set(duanzi_dict['zan'], duanzi_dict['floor'])
    pass
gen_top_rank_duanzi_floor_list()
rename_top_list_name_for_web()



