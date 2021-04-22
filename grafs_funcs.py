import matplotlib
import matplotlib.pyplot as plt


def make_png_holt(data_list, prognos_list, png_dir, x, alfa, beta):
    '''
    Make graf with data and "Exponential smoothing based on the trend" and save it to png file.
    :param data_list: ['kod_gup', 'art.', 'name', data_1, ... data_n]
    :param prognos_list: ['kod_gup', 'art.', 'name', prognos_1, ... prognos_n]
    :param png_dir: directory
    :param x: month list
    :return: make png file (filename = 'kod_gup')
    '''
    x_data = x
    x_prognos = x[1:]
    x_prognos.append('след. шаг')
    graf_name = f'''{prognos_list[0]}, {data_list[2]}'''
    filename = data_list[0]
    y = prognos_list[3:]
    z = data_list[3:]
    fig, ax1 = plt.subplots(figsize=(12, 8))
    fig.subplots_adjust(bottom=0.2, left=0.1)
    ax1.set_title(graf_name)
    ax1.annotate(f'''Прогноз на следующий шаг: {prognos_list[-1]}, при a = {alfa}, b = {beta}. Исходные данные за период с {x[0]} по {x[-1]}''',
                 xy=(25, 25), xycoords='figure pixels')
    ax1.annotate(
    f'{prognos_list[-1]}',
    xy=(x_prognos[-1], y[-1]), xycoords='data',
    xytext=(15, 0), textcoords='offset points')#,
    # arrowprops=dict(arrowstyle="->"))
    plt.plot(x_data, z, label='Исходные данные', color='#98FB98')
    plt.plot(x_prognos, y, label='Скользящая средняя', color='#006400')
    plt.xlabel('Среднемесячные значения')
    plt.ylabel('Количество')
    plt.tick_params(axis='x', rotation=70)
    # ax2 = ax1.twinx()
    # ax1.set_title(graf_name)
    line_up, = ax1.plot(x_data, z, label='Исходные данные', color='#98FB98')
    line_down, = ax1.plot(x_prognos, y, label=f'Скользящая средняя', color='#006400')
    plt.legend(handles=[line_up, line_down])
    plt.xlim(0, len(x_data))
    # ax1.set_xlabel('Среднемесячные значения')
    # ax1.set_ylabel('Количество')
    # ax2.set_xlabel('2')
    # ax2.set_ylabel('Количество')
    # ax1.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    # ax1.tick_params(axis='x', rotation=70)
    plt.savefig(f'{png_dir}{filename}.png', dpi=200)
    plt.close('all')
