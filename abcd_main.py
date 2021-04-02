from read_file import *
from abcd_func import *


# Input year and column name
abcd_year = 2020
col_name = 'cost'   # 'count' or 'cost'

# start ABCD
tmp_index_dict = otbor_indexov(index_dict, abcd_year, col_name)
new_list, prihod_list, rashod_list, kon_ostatok_list = make_new_list_abcd(main_list, tmp_index_dict)
result_list = abcd(new_list, prihod_list, 3)
result_list = abcd(new_list, rashod_list, 4)
result_list = abcd(new_list, kon_ostatok_list, 5)
if __name__ == '__main__':
    write_csv_r(result_list, f'abcd_{abcd_year}')
