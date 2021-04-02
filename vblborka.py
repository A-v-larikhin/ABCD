from read_file import *
from read_file import write_float_with_point as rf


def make_x_indexes(index_dict, col_name):
    for key in index_dict:
        if key == col_name:
            list = index_dict[key]
    return list

def make_x_lists(list, data_type):
    date_list = []
    data_list = []
    if data_type == 'cost':
        foo = 2
    elif data_type == 'count':
        foo = 1
    for item in list:
        date_list.append(item[0])
        data_list.append(item[foo])
    return date_list, data_list

filename = 'vblborka'
gup_kods = make_gup_kods()
col_name = 'rashod_i'
data_type = 'count'
x_index_list = make_x_indexes(index_dict, col_name)
date_list, data_i_list = make_x_lists(x_index_list, data_type)
result_list = [[main_list[0][1], main_list[0][2], main_list[0][3], main_list[0][4]]]
for item in date_list:
    result_list[0].append(item.strftime("%m/%Y"))

for gup_kod in gup_kods:
    for row in main_list:
        if row[1] == gup_kod:
            tmp_list = [row[1], row[2], row[3], row[4]]
            for index in data_i_list:
                tmp_list.append(rf(row[index]))
            result_list.append(tmp_list)

if __name__ == '__main__':
    for row in result_list:
        print(row)
    write_csv_r(result_list, filename)
