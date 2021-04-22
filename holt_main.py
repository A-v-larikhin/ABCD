from read_file import *
from holt_funcs import *
from grafs_funcs import make_png_holt

# Input column name, directory name for *.png
col_name = 'rashod_i'   # 'count' or 'cost'
png_dir = './png_holt/'
csv_file = './result/holt_01_half_year_2021.csv'
period = 6 # must be integer (month = 1, quarter = 3, half_year = 6 )

# main_list from vblborka
gup_kods = make_gup_kods()
new_list = main_list[0:3]
for row in main_list:
    for gup_kod in gup_kods:
        if row[1] == gup_kod:
            new_list.append(row)
main_list = new_list

# Start Holt
if __name__ == '__main__':
    holt_index_list, month_list = otbor_indexov_holt(index_dict, col_name)
    if period == 1:
        holt_month_func(main_list, holt_index_list, png_dir, csv_file, month_list)
    else:
        main_list = make_small_list(main_list, holt_index_list)
        period_list = holt_period_list(holt_index_list, period)
        main_list = holt_average_list(main_list, period)
        holt_period_func(main_list, png_dir, csv_file, period_list)
        for row in main_list:
            print(row)
        print(period_list)
