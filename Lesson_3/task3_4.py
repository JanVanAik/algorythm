array = input('Введите числа через запятую: ').split(',')
array = [int(i) for i in array]
max_num = array[0]
for i in array:
    if array.count(i) > array.count(max_num):
        max_num = i
print(f'Число  {max_num} встречается больше всего раз')
