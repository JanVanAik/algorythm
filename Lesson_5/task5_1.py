import collections


def dict_gen(amount):
    my_dicts = collections.defaultdict(dict)
    for i in range(amount):
        summa = 0
        number = 0
        name = input('Введите название предприятия: ')
        quarters = input('Введите через запятую прибыль для каждого квартала: ').replace(' ', '').split(',')
        my_dicts[name] = {}
        for k, v in my_dicts.items():
            if k == name:
                for index, elem in enumerate(quarters):
                    v[f'{index + 1} квартал'] = elem
                    summa += int(elem)
                    number += 1
        avrg = summa / number
    return my_dicts, avrg


my_dict = dict_gen(int(input('Введите количество предприятий: ')))


def avg_count(dictionary, average):
    for k, v in dictionary.items():
        summa = 0
        for val in v.values():
            summa += int(val)
        avg = summa / 4
        if avg < average:
            print(f'Компания {k} заработала {avg} - меньше среднего по всем предприятиям - {average}')
        else:
            print(f'Компания {k} заработала {avg} - больше среднего по всем предприятиям - {average}')


avg_count(my_dict[0], my_dict[1])
