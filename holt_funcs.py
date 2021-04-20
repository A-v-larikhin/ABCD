def holt_main_func(main_list, holt_index_list):
    '''
    Make dict with prognosis list
    :param main_list:
    :param holt_index_list:
    :return: holt dict { 'kod_gup' : [[name, ed. izm.], [data list], [prognosis list]]}
    '''
    rows = len(main_list) - 1
    holt_dict = {}
    for row in range(3, rows):
        row_name = main_list[row][1]
        row_descript = main_list[row][2:4]
        row_data = []
        for list in holt_index_list:
            col = list[1]
            row_data.append(main_list[row][col])
        row_prognos = calculation(row_data)
        holt_dict[row_name] = [row_descript, row_data, row_prognos]
    return holt_dict


def calculation(list):
    '''
    Calculation with iteration of parameters alfa & betta in "Exponential smoothing based on the trend"
    :param list: data list
    :return: prognosis list
    '''
    sigmax = 0
    for k in range(1, 11):
        for j in range(1, 11):
            a = k / 10; b = j / 10; ft = []; st = []; yt = []; sig = []
            ft.append(list[0])
            st.append(0)
            for i in range(1, len(list)):
                ft.append(a*list[i] + (1 - a)*(ft[i-1] + st[i-1]))
                st.append(b * (ft[i] - ft[i-1]) + (1-b)*st[i-1])
                yt.append(ft[i-1] + st[i-1])
                sig.append((list[i] - yt[i-1])**2)
            sigma = (sum(sig)/len(sig))**0.5
            if sigmax == 0 or sigma < sigmax:
                sigmax = sigma
                alfa = a
                beta = b
                prognos_list = yt
    return prognos_list


def otbor_indexov_holt(index_dict, col_name):
    '''
    Make list of indexes from index_dict. Отбор по названию столбца (приход, расход, кон. остаток).
    :param: index_dict, col_name (one of: 'nach_ostatok_i', 'prihod_i', 'rashod_i', 'kon_ostatok_i')
    :return: list of indexes [[date, count index, cost index], [date, count index, cost index], ....]
    '''
    holt_index_list = []
    for item in index_dict:
        if item == col_name:
            holt_index_list = index_dict[item]
    return holt_index_list