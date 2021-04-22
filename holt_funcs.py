from grafs_funcs import make_png_holt
import csv

def holt_month_func(main_list, holt_index_list, png_dir, csv_file, x):
    '''
    Make dict with prognosis list
    :param main_list:
    :param holt_index_list:
    :return: holt dict { 'kod_gup' : [[name, ed. izm.], [data list], [prognosis list], alfa, beta]}
    '''
    with open(csv_file, 'w', encoding='cp1251') as file:
        writer = csv.writer(file, delimiter=';', quotechar='"')
        rows = len(main_list) - 1
        #holt_dict = {}
        for row in range(3, rows):
            #row_name = main_list[row][1]
            #row_descript = main_list[row][2:4]
            row_data = []
            for list in holt_index_list:
                col = list[1]
                row_data.append(main_list[row][col])
            row_prognos, alfa, beta = calculation(row_data)
            #holt_dict[row_name] = [row_descript, row_data, row_prognos, alfa, beta]
            data_list = main_list[row][1:4]
            data_list.extend(row_data)
            prognos_list = main_list[row][1:4]
            prognos_list.extend(row_prognos)
            csv_str = main_list[row][1:4]
            csv_str.append(prognos_list[-1])
            writer.writerow(csv_str)
            make_png_holt(data_list, prognos_list, png_dir, x, alfa, beta)
    #return holt_dict


def calculation(list):
    '''
    Calculation with iteration of parameters alfa & betta in "Exponential smoothing based on the trend"
    :param list: data list
    :return: prognosis list
    '''
    sigmax = 0
    for k in range(0, 101):
        for j in range(0, 101):
            a = k / 100; b = j / 100; ft = []; st = []; yt = []; sig = []
            ft.append(sum(list)/len(list)) # ft.append(list[0])
            st.append(0)
            for i in range(1, len(list)):
                ft.append(a*list[i] + (1 - a)*(ft[i-1] + st[i-1]))
                st.append(b * (ft[i] - ft[i-1]) + (1-b)*st[i-1])
                yt.append(ft[i-1] + st[i-1])
                sig.append((list[i] - yt[i-1])**2)
            yt.append(round(ft[-1] + st[-1]))
            sigma = (sum(sig)/len(sig))**0.5
            if sigmax == 0 or sigma < sigmax:
                sigmax = sigma
                alfa = a
                beta = b
                prognos_list = yt
    return prognos_list, alfa, beta


def otbor_indexov_holt(index_dict, col_name):
    '''
    Make list of indexes from index_dict. Отбор по названию столбца (приход, расход, кон. остаток).
    :param: index_dict, col_name (one of: 'nach_ostatok_i', 'prihod_i', 'rashod_i', 'kon_ostatok_i')
    :return: list of indexes [[date, count index, cost index], [date, count index, cost index], ....]
    and month list
    '''
    month_list = []
    holt_index_list = []
    for item in index_dict:
        if item == col_name:
            holt_index_list = index_dict[item]
            for i in holt_index_list:
                month_list.append(i[0].strftime("%m/%Y"))
    return holt_index_list, month_list


def holt_average_list(main_list, period):
    '''
    Make list with average for the period
    :return: ['kod_gup', 'art.', 'name', count1, count2, ...., count_n]
    '''
    new_main_list = []
    cols = len(main_list[0])
    for row in main_list:
        tmp_list = row[0:3]
        for col in range(3, cols, period):
            period_sum = 0
            for i in range(period):
                period_sum += row[col + i]
            average = round(period_sum / period)
            tmp_list.append(average)
        new_main_list.append(tmp_list)
    return new_main_list


def make_small_list(main_list, holt_index_list):
    '''
    :return: ['kod_gup', 'art.', 'name', count1, count2, ...., count_n]
    '''
    new_list = []
    rows = len(main_list) - 1
    for row in range(3, rows):
        tmp_list = main_list[row][1:4]
        for i in holt_index_list:
            col = i[1]
            tmp_list.append(main_list[row][col])
        new_list.append(tmp_list)
    return new_list


def holt_period_list(holt_index_list, period):
    period_list = []
    list_length = len(holt_index_list)
    section = f'/{round(12 / period)}'
    x = 0
    for i in range(0, list_length, period):
        x += 1
        if x > round(12 / period):
            x=1
        period_list.append(f'{x}{section} {holt_index_list[i][0].strftime("%Y")}')
    return period_list


def holt_period_func(main_list, png_dir, csv_file, x):
    '''
    Make csv with prognosis and *.png files
    :param main_list:
    :param x: period list
    '''
    with open(csv_file, 'w', encoding='cp1251') as file:
        writer = csv.writer(file, delimiter=';', quotechar='"')
        for row in main_list:
            row_data = row[3:]
            row_prognos, alfa, beta = calculation(row_data)
            data_list = row[0:3]
            data_list.extend(row_data)
            prognos_list = row[0:3]
            prognos_list.extend(row_prognos)
            csv_str = row[0:3]
            csv_str.append(prognos_list[-1])
            writer.writerow(csv_str)
            print(data_list)
            print(prognos_list)
            print(x)
            make_png_holt(data_list, prognos_list, png_dir, x, alfa, beta)