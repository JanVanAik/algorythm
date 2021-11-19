import random

choice = input('Вы хотите случайное число(1), вещественное число(2) или символ(3)? Введите 1, 2 или 3, чтобы выбрать: ')
if choice == '1':
    lower = input('Введите нижнюю границу предела: ')
    upper = input('Введите верхнюю границу предела: ')
    if lower.isdigit() and upper.isdigit():
        print(random.randint(int(lower), int(upper)))
    else:
        print('Вы ввели не число')
elif choice == '2':
    lower = input('Введите нижнюю границу предела: ').replace(',', '.')
    upper = input('Введите верхнюю границу предела: ').replace(',', '.')
    if lower.replace('.', '').isdigit() and upper.replace('.', '').isdigit():
        lower = float(lower)
        upper = float(upper)
        print(round(random.uniform(lower, upper), 2))
elif choice == '3':
    my_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }
    lower = input('Введите нижнюю границу предела - английскую букву: ')
    upper = input('Введите верхнюю границу предела- английскую букву: ')
    dict_list = 'abcdefghijklmnopqrstuvwxyz'
    print(dict_list[dict_list.find(lower):dict_list.find(upper)+1])
else:
    print('Вы не выбрали. Пожалуйста, сначала думайте, потом пишите.')
