from read_file import *


def read_float_with_comma(num):
    return float(num.replace(",", "."))


def make_null(main_list):
    '''
    Insert 0 in empty cells
    :param main_list: main_list
    :return: main_list
    '''
    cols = 0
    cols += len(main_list[3])
    rows = len(main_list)
    for row in range(3, rows):
        for col in range(5, cols):
            if main_list[row][col] == '':
                main_list[row][col] = 0
            else:
                main_list[row][col] = read_float_with_comma(main_list[row][col])
    return main_list


def otbor_indexov(index_dict, year, col_2name):
    '''
    Make list of indexes from index_dict. Отбор по году и названию столбца (приход, расход, кон. остаток).
    :param: index_dict, year (YYYY),
     col_2name ('count', 'cost')
    :return: lists of indexes in tmp_index_dict
    '''
    tmp_index_dict = {}
    for item in index_dict:
        tmp_index_list = []
        if item != 'nach_ostatok_i':
            tmp_list = index_dict[item]
            for i in tmp_list:
                if year == i[0].year:
                    if col_2name == 'count':
                        tmp_index_list.append(i[1])
                    elif col_2name == 'cost':
                        tmp_index_list.append(i[2])
            tmp_index_dict[item] = tmp_index_list
    return tmp_index_dict


def make_new_list(main_list, tmp_index_dict):
    '''
    make new list.
    :param: main_list, list of indexes
    :return: new_list
    '''
    new_list = [['КодГуп', 'Артикул', 'Номенклатура', 'приход', 'расход', 'кон. остаток', 'ABCD']]
    prihod_list = []
    rashod_list = []
    kon_ostatok_list = []
    rows = len(main_list) - 1
    for row in range(3, rows):
        new_list.append([main_list[row][1], main_list[row][2], main_list[row][3], 0, 0, 0, ''])
        for item in tmp_index_dict:
            if item == 'prihod_i':
                for col in tmp_index_dict[item]:
                    new_list[row-2][3] += main_list[row][col]
            elif item == 'rashod_i':
                for col in tmp_index_dict[item]:
                    new_list[row-2][4] += main_list[row][col]
            elif item == 'kon_ostatok_i':
                for col in tmp_index_dict[item]:
                    new_list[row-2][5] = main_list[row][col]
    for row in range(1, len(new_list)):
        prihod_list.append(new_list[row][3])
        rashod_list.append(new_list[row][4])
        kon_ostatok_list.append(new_list[row][5])
    return new_list, prihod_list, rashod_list, kon_ostatok_list


def make_borders(list):
    sumi = 0
    count = 0
    for i in list:
        if i > 0:
            sumi += i
            count += 1
    border_ab = sumi / count
    sumi = 0
    count = 0
    for i in list:
        if 0 < i < border_ab:
            sumi += i
            count += 1
    border_bc = sumi / count
    return border_ab, border_bc


def abcd(new_list, list, num):
    """

    :param new_list:
    :param list:
    :param num:
    :return:
    """
    rows = len(new_list)
    pr_ab, pr_bc = make_borders(list)
    print(str(pr_ab) + " - " + str(pr_bc))
    for row in range(1, rows):
        if new_list[row][num] >= pr_ab:
            new_list[row][6] += 'A'
        elif pr_bc <= new_list[row][num] < pr_ab:
            new_list[row][6] += 'B'
        elif new_list[row][num] < 0.000000001:
            new_list[row][6] += 'D'
        else:
            new_list[row][6] += 'C'
    return new_list
