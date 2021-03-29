from read_file import *
from abcd import *

if __name__ == '__main__':
# start ABCD
    abcd_year = 2020
    tmp_index_dict = otbor_indexov(index_dict, abcd_year, 'cost')
    new_list, prihod_list, rashod_list, kon_ostatok_list = make_new_list_abcd(main_list, tmp_index_dict)
    result_list = abcd(new_list, prihod_list, 3)
    result_list = abcd(new_list, rashod_list, 4)
    result_list = abcd(new_list, kon_ostatok_list, 5)
    write_csv_r(result_list, f'abcd_{abcd_year}')
    #for row in result_list:
        #print(row[0])
# finish ABCD
# ----------------
# start XYZ
