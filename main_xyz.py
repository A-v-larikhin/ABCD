from read_file import *
from xyz import *

if __name__ == '__main__':
    result_list = row_mean_to_new_list(main_list, rashod_i)
    result_list = dispersion_to_new_list(main_list, result_list, rashod_i)
    result_list = make_xyz(result_list)
    for row in result_list:
        print(row)
    write_csv_r(result_list, 'xyz')