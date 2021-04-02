from abcd_main import result_list as abcd_list
from xyz_main import result_list as xyz_list
from read_file import write_float_with_point as rf
from read_file import write_csv_r

filename = 'abcd_xyz_2020'
result_list = [['КодГуп', 'Артикул', 'Номенклатура', 'приход', 'расход', 'кон. остаток', 'ABCD',
                'Ср. арифм.', 'Коэфф. вариации', 'XYZ']]
for abcd_row in abcd_list:
    for xyz_row in xyz_list:
        if abcd_row[0] == xyz_row[0]:
            abcd_row[3] = rf(abcd_row[3])
            abcd_row[4] = rf(abcd_row[4])
            abcd_row[5] = rf(abcd_row[5])
            abcd_row.append(rf(xyz_row[3]))
            abcd_row.append(rf(xyz_row[6]))
            abcd_row.append(rf(xyz_row[7]))
            result_list.append(abcd_row)

if __name__ == '__main__':
    for row in result_list:
        print(row)
    write_csv_r(result_list, filename)
