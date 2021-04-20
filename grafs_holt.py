from holt_main import holt_dict, month_list
from grafs_funcs import make_png_file

dir = './png_holt/'
if __name__ == '__main__':
    for item in holt_dict:
        data_list = []
        prognos_list = []
        data_list.append(item)
        data_list.extend(holt_dict[item][0])
        data_list.extend(holt_dict[item][1])
        prognos_list.append(item)
        prognos_list.extend(holt_dict[item][0])
        prognos_list.extend(holt_dict[item][2])
        make_png_file(data_list, prognos_list, dir, month_list)
        print(data_list)
        print(prognos_list)
