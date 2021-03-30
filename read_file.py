import csv
from datetime import date

__all__ = ['main_list', 'index_dict', 'make_index_list',
           'write_csv_r']

# Data DIR
FILES_DIR = './files/'
# Data File
file_main = FILES_DIR + 'ABCD_avtozapchasti2.csv'

def read_csv_list(file_name):
    with open(file_name, encoding='cp1251', newline='') as f:
    #with open(file_name, newline='') as f:
        reader = csv.reader(f, delimiter=';')
        data = list(reader)
    return data


def read_float_with_comma(num):
    return float(num.replace(",", "."))


def make_null(main_list):
    '''
    Insert 0 in empty cells
    :param main_list: main_list
    :return: main_list
    '''
    cols = len(main_list[3])
    rows = len(main_list)
    for row in range(3, rows):
        for col in range(5, cols):
            if main_list[row][col] == '':
                main_list[row][col] = 0
            else:
                main_list[row][col] = read_float_with_comma(main_list[row][col])
    return main_list

# Make main list with '0'
main_list = read_csv_list(file_main)
main_list = make_null(main_list)

rows = len(main_list) - 1
cols = len(main_list[3])

month_dict = {'Январь': 1, 'Февраль': 2, 'Март': 3, 'Апрель': 4, 'Май': 5, 'Июнь': 6, 'Июль': 7, 'Август': 8, 'Сентябрь': 9, 'Октябрь': 10, 'Ноябрь': 11, 'Декабрь': 12}

# Make dict of indexes
index_dict = {'nach_ostatok_i':[], 'prihod_i':[], 'rashod_i':[], 'kon_ostatok_i':[]}
for item in main_list[0]:
    for _month_ in month_dict:
        if _month_ in item:
            _mm_ = int(month_dict[item.split()[0]])
            _yyyy_ = int(item.split()[1])
            d = date(_yyyy_, _mm_, 15)
            index_dict['nach_ostatok_i'].append([d, main_list[0].index(item), main_list[0].index(item) + 1])
            index_dict['prihod_i'].append([d, main_list[0].index(item) + 2, main_list[0].index(item) + 3])
            index_dict['rashod_i'].append([d, main_list[0].index(item) + 4, main_list[0].index(item) + 5])
            index_dict['kon_ostatok_i'].append([d, main_list[0].index(item) + 6, main_list[0].index(item) + 7])

def make_index_list(index_dict, date1, date2, col_name, type):
    list = []
    num = 0
    if type == 'count':
        num = 1
    elif type == 'cost':
        num = 2
    else:
        print('Must be "count" or "cost"')
    for key in index_dict:
        if key == col_name:
            for item in index_dict[key]:
                if date1 <= item[0] <= date2:
                        list.append(item[num])
    return list


def write_csv_r(data, file):
    '''
    Make result file
    :param data: list
    :param file: file 'name'
    :return: write file
    '''
    with open(f'./result/{file}.csv', 'w', encoding = 'cp1251'
              ) as file:
        writer = csv.writer(file, delimiter=';', quotechar='"')
        for i in data:
            writer.writerow(i)