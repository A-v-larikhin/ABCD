from read_file import *
from holt_funcs import *


# Input year and column name
col_name = 'rashod_i'   # 'count' or 'cost'

# Start Holt
holt_index_list = otbor_indexov_holt(index_dict, col_name)
holt_dict = holt_main_func(main_list, holt_index_list)


if __name__ == '__main__':
    holt_dict = holt_main_func(main_list, holt_index_list)
    for item in holt_dict:
        data_list = []
        prognos_list = []
        data_list.append(item)
        data_list.extend(holt_dict[item][0])
        data_list.extend(holt_dict[item][1])
        prognos_list.append(item)
        prognos_list.extend(holt_dict[item][0])
        prognos_list.extend(holt_dict[item][1])
        #write_csv_r(data_list, f'holt_')
        #write_csv_r(prognos_list, f'holt_')