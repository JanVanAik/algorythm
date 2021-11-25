import random

array = [(random.randint(1, 100)) for i in range(10)]
min_i = array.index(min(array))
max_i = array.index(max(array))
sum_array = 0
if max_i < min_i:
    max_i, min_i = min_i, max_i
for i, v in enumerate(array):
    if i in range(min_i + 1, max_i):
        sum_array += v
print(f' Массив: {array}, сумма элементов между минимальным и максимальным: {sum_array}')
