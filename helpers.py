from read_file import read_csv_list

def make_gup_kods():
    list = read_csv_list('./files/x.csv')
    gup_kods = []
    for row in list:
        gup_kods.append(row[0])
    return gup_kods
