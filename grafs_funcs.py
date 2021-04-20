import matplotlib
import matplotlib.pyplot as plt


def make_png_file(data_list, prognos_list, dir, x):
    '''
    Make graf with data and "Exponential smoothing based on the trend" and save it to png file.
    :param data_list: ['kod_gup', 'art.', 'name', data_1, ... data_n]
    :param prognos_list: ['kod_gup', 'art.', 'name', prognos_1, ... prognos_n]
    :param dir: directory
    :param x: month list
    :return: make png file (filename = 'kod_gup')
    '''
    graf_name = f'{prognos_list[0]}, {data_list[2]}'
    filename = data_list[0]
    y = prognos_list[3:]
    z = data_list[3:]
    fig, ax1 = plt.subplots(figsize=(12, 8))
    fig.subplots_adjust(bottom=0.15, left=0.2)
    ax1.set_title(graf_name)
    plt.plot(x,y, label='Скользящая средняя', color='#006400')
    plt.plot(x,z, label='Исходные данные', color='#98FB98')
    plt.xlabel('Среднемесячные значения')
    plt.ylabel('Количество')
    plt.tick_params(axis='x', rotation=70)
    #ax2 = ax1.twinx()
    #ax1.set_title(graf_name)
    line_up, = ax1.plot(x, z, label='Исходные данные', color='#98FB98')
    line_down, = ax1.plot(x, y, label='Скользящая средняя', color='#006400')
    plt.legend(handles=[line_up, line_down])
    #ax1.set_xlabel('Среднемесячные значения')
    #ax1.set_ylabel('Количество')
    # ax2.set_xlabel('2')
    # ax2.set_ylabel('Количество')
    #ax1.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    #ax1.tick_params(axis='x', rotation=70)
    plt.savefig(f'{dir}{filename}.png', dpi=200)
    plt.close('all')