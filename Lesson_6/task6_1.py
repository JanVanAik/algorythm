import random
import math
from memory_profiler import profile


# from task  3.6

@profile
def array_counter():
    array = [(random.randint(1, 100)) for i in range(10)]
    min_i = array.index(min(array))
    max_i = array.index(max(array))
    sum_array = 0
    if max_i < min_i:
        max_i, min_i = min_i, max_i
    for i, v in enumerate(array):
        if i in range(min_i + 1, max_i):
            sum_array += v
    return array, sum_array


res = array_counter()
arr = res[0]
summ = res[1]
print(f' Массив: {arr}, сумма элементов между минимальным и максимальным: {summ}')


# from task 3.9


@profile
def matrix_gen(column, row):
    matrix = []
    for i in range(row):
        m_string = []
        for j in range(column - 1):
            num = random.randint(0, 100)
            m_string.append(num)
        m_string.append(sum(m_string))
        matrix.append(m_string)
    return matrix


@profile
def print_matrix(column, row):
    matrix = matrix_gen(column, row)
    for k in range(row):
        for x in range(column):
            print(matrix[k][x], end=' ')
        print()


@profile
def main():
    column = 500
    row = 400
    print_matrix(column, row)


print(main())


# from task 4.2


@profile
def eratosthenes(n, pos):
    sieve = list(range(n + 1))
    sieve[1] = 0
    counter = 0
    for i in sieve:
        if i > 1:
            # counter += 1
            # if counter == pos:
            #     return i
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve


number = int(input('Введите номер простого числа: '))
amount = 10
while number > amount / math.log(amount):
    amount += 100
print(amount)
print(eratosthenes(amount, number))

# Как можно заметить - большая часть программ не занимает много памяти даже на больших числах.
# Значимые запросы памяти можно отметить в функции main, когда выполняется печать матрицы. Однако я не вижу здесь
# больших возможностей для оптимизации, так как функция с двумя переменными, которые перемножаются ( двойной цикл)
# Конкретно больше всего памяти, в итоге, съедает  вот эта строка
# 38     16.5 MiB      1.7 MiB      199600               m_string.append(num)
# То есть самое дорогое - внесение в список нового элемента.
