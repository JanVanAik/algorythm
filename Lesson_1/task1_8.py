year = input('Введите год: ')
if year.isdigit():
    year = int(year)
    if year % 4 == 0 and year % 100 == 0:
        if year % 400 == 0:
            print('Високосный')
        else:
            print('Невисокосный')
    elif year % 4 == 0:
        print('Високосный')
    else:
        print('Невисокосный')
else:
    print('Это не число')
