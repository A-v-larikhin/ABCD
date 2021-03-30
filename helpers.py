from abcd_main import main_list, index_dict, kon_ostatok_i

month_dict = {}
month_num = 1
for item in main_list[0]:
    if '2020' in item:
        month_dict[item.split()[0]] = month_num
        month_num += 1
print(month_dict)

for item in index_dict:
    print(f'{len(index_dict[item])} - {item}')

print(kon_ostatok_i[-1])