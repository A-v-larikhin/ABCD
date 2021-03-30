def row_mean_to_new_list(main_list, index_list):
    new_list = [['КодГуп', 'Артикул', 'Номенклатура', 'Ср. арифм.', 'Дисперсия', 'СКО', 'Коэфф. вариации', 'XYZ']]
    rows = len(main_list) - 1
    for row in range(3, rows):
        row_sum = 0
        for col in index_list:
            row_sum += main_list[row][col]
        row_mean = row_sum/len(index_list)
        new_list.append([main_list[row][1], main_list[row][2], main_list[row][3], row_mean, 0, 0, 0, ''])
    return new_list

def dispersion_to_new_list(main_list, new_list, index_list):
    rows = len(main_list) - 1
    for row in range(3, rows):
        row_disp_sum = 0
        for col in index_list:
            mean = new_list[row - 2][3]
            row_disp_sum += (mean - main_list[row][col]) ** 2
        dispersion = row_disp_sum/len(index_list)
        sko = dispersion ** (1/2)
        if new_list[row-2][3] > 0:
            k_var = sko / new_list[row-2][3] * 100
        else:
            k_var = 'D'
        new_list[row-2][4] = dispersion
        new_list[row-2][5] = sko
        new_list[row-2][6] = k_var
    return new_list

def make_xyz(new_list):
    for row in range(1, len(new_list)):
        if type(new_list[row][6]) != str and new_list[row][6] < 10:
            new_list[row][7] = 'X'
        elif type(new_list[row][6]) != str and 10 < new_list[row][6] < 25:
            new_list[row][7] = 'Y'
        elif type(new_list[row][6]) != str and new_list[row][6] > 25:
            new_list[row][7] = 'Z'
        elif type(new_list[row][6]) == str:
            new_list[row][7] = ''
    return new_list