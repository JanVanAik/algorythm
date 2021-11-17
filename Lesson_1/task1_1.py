num = input('Введите трехзначное число: ')
if num.isdigit() is True:
    if int(num)//100 >= 1 and int(num)//100 <=9:
        print(f'Ответ: {int(num[0]) * int(num[1]) * int(num[2])}')
    else:
        print('Не трехзначное')
else:
    print('Не число')
