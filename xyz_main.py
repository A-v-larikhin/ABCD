from read_file import *
from xyz_func import *


# Input a date range
date_range = [2020, 1, 2020, 12]    # exmpl: [2020, 1, 2020, 12]   -     2020, january - 2020, december

# Input a column name
col_name1 = 'rashod_i'   # 'nach_ostatok_i' or 'prihod_i' or 'rashod_i' or 'kon_ostatok_i'
col_name2 = 'count'      # 'count' or 'cost'

# Input a filename
filename = 'xyz_2020'    # without extension

# start XYZ
i_list = make_index_list(index_dict, date_range, col_name1, col_name2)
result_list = row_mean_to_new_list(main_list, i_list)
result_list = dispersion_to_new_list(main_list, result_list, i_list)
result_list = make_xyz(result_list)
for row in result_list:
    print(row)
write_csv_r(result_list, filename)
