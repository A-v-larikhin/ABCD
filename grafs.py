import matplotlib
import matplotlib.pyplot as plt
from vblborka import result_list, result_list2
from read_file import read_float_with_comma as rfc

cols = len(result_list[0])
rows = len(result_list)
for row in range(1, rows):
    tmp_list = [result_list[row][0], result_list[row][1], result_list[row][2], result_list[row][3]]
    tmp_list2 = [result_list[row][0], result_list[row][1], result_list[row][2], result_list[row][3]]
    for col in range(4, cols):
        num = float(result_list[row][col])
        num2 = float(result_list2[row][col])
        tmp_list.append(num)
        tmp_list2.append(num2)
    result_list[row] = tmp_list
    result_list2[row] = tmp_list2

x = result_list[0][4:]
for row in range(1, rows):
    graf_name = f'{result_list[row][0]}, {result_list[row][2]}'
    filename = result_list[row][0]
    y = result_list[row][4:]
    z = result_list2[row][4:]
    fig, ax1 = plt.subplots(figsize=(12, 8))
    fig.subplots_adjust(bottom=0.15, left=0.2)
    ax2 = ax1.twinx()
    ax1.set_title(graf_name)
    line_up, = ax1.plot(x, z, label='Стоимость', color='#98FB98')
    line_down, = ax2.plot(x, y, label='Количество', color='#006400')
    plt.legend(handles=[line_up, line_down])
    ax1.set_xlabel('Среднемесячные значения')
    ax1.set_ylabel('Стоимость, руб.')
    # ax2.set_xlabel('2')
    ax2.set_ylabel('Количество')
    ax1.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax1.tick_params(axis='x', rotation=70)
    plt.savefig(f'./png_vblborka/{filename}.png', dpi=200)
    plt.close('all')
