array = input('Введите числа через запятую: ').split(',')
array = [int(i) for i in array]
minimum = min(array)
for i, v in enumerate(array):
    if v < 0:
        if v > minimum:
            res = (i, v)
print(res)
