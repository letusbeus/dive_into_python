from modules import *

if __name__ == '__main__':
    date = argv[1] if len(argv) > 1 else input('Введите дату вручную: ')
    if calendar(date):
        print(calendar(date))
    else:
        print('Дата не верна')
