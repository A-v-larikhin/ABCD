import csv
from datetime import date


class ReadFile:
    # Data DIR and File
    FILES_DIR = './files/'
    file_name = FILES_DIR + 'ABCD_avtozapchasti2.csv'

    # rows = len(main_list) - 1
    # cols = len(main_list[3])

    @staticmethod
    def read_csv_list():
        with open(ReadFile.file_name, encoding='cp1251', newline='') as f:
        #with open(file_name, newline='') as f:
            reader = csv.reader(f, delimiter=';')
            data = list(reader)
        return data

    @staticmethod
    def read_float_with_comma(num):
        return float(num.replace(",", "."))


    #@classmethod
    def make_null():
        '''
        Insert 0 in empty cells
        :return: main_list
        '''
        main_list = ReadFile.read_csv_list()
        cols = len(main_list[3])
        rows = len(main_list)
        for row in range(3, rows):
            for col in range(5, cols):
                if main_list[row][col] == '':
                    main_list[row][col] = 0
                else:
                    main_list[row][col] = ReadFile.read_float_with_comma(main_list[row][col])
        return main_list


def make_indexes(list, data_start, data_end):
    month_dict = {'Январь': 1, 'Февраль': 2, 'Март': 3, 'Апрель': 4, 'Май': 5, 'Июнь': 6, 'Июль': 7, 'Август': 8,
                  'Сентябрь': 9, 'Октябрь': 10, 'Ноябрь': 11, 'Декабрь': 12}
    nach_ostatok_i = []
    prihod_i = []
    rashod_i = []
    kon_ostatok_i = []
    index_dict = {'nach_ostatok_i': [], 'prihod_i': [], 'rashod_i': [], 'kon_ostatok_i': []}
    for item in list[0]:
        for _month_ in month_dict:
            if _month_ in item:
                _mm_ = int(month_dict[item.split()[0]])
                _yyyy_ = int(item.split()[1])
                d = date(_yyyy_, _mm_, 15)
                if data_start <= d <= data_end:
                    nach_ostatok_i.append(list[0].index(item))
                    prihod_i.append(list[0].index(item) + 2)
                    rashod_i.append(list[0].index(item) + 4)
                    kon_ostatok_i.append(list[0].index(item) + 6)
                    # -----
                    index_dict['nach_ostatok_i'].append([d, list[0].index(item), list[0].index(item) + 1])
                    index_dict['prihod_i'].append([d, list[0].index(item) + 2, list[0].index(item) + 3])
                    index_dict['rashod_i'].append([d, list[0].index(item) + 4, list[0].index(item) + 5])
                    index_dict['kon_ostatok_i'].append([d, list[0].index(item) + 6, list[0].index(item) + 7])
    return index_dict


def write_csv_r(data, file):
    '''
    Make result file
    :param data: list
    :param file: file name
    :return: write file to os
    '''
    with open(f'./result/{file}.csv', 'w', encoding = 'cp1251'
              ) as file:
        writer = csv.writer(file, delimiter=';', quotechar='"')
        for i in data:
            writer.writerow(i)

