from datetime import date
from read_file import *
from xyz import *

i_list = make_index_list(index_dict, date(2020,1,15), date(2020,12,15), 'rashod_i', 'count')
result_list = row_mean_to_new_list(main_list, i_list)
result_list = dispersion_to_new_list(main_list, result_list, i_list)
result_list = make_xyz(result_list)
for row in result_list:
    print(row)
write_csv_r(result_list, 'xyz_2020')