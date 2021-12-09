from random import randint
import cProfile


# варинт

def array_gen(start, end, m):
    array = []
    for i in range(2 * m + 1):
        array.append(randint(start, end))
    return array


def array_sort(array):
    if len(array) == 1:
        return array[:]
    else:
        middle = len(array) // 2
        left = array_sort(array[:middle])
        right = array_sort(array[middle:])
        return array_merge(left, right)


def array_merge(left, right):
    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            res.append(right[j])
            j += 1
        else:
            res.append(left[i])
            i += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res


def main1():
    my_array = array_gen(-100, 100, 10000)
    array_sorted = array_sort(my_array)
    return array_sorted

def main2():
    my_array = array_gen(-100, 100, 10000)
    result = []
    for i in range(len(my_array) // 2 + 1):
        result.append(min(my_array))
        my_array.remove(min(my_array))
    return f'Медиана с индексом {len(my_array) // 2}, равна {result[-1]}'


my_array = array_gen(-100, 100, 5)
array_sorted = array_sort(my_array)
print(my_array)
print(array_sorted)
print(f'Медиана с индексом {len(array_sorted) // 2}, стоящая  равна {array_sorted[len(array_sorted) // 2]}')

'''
Проверка затрат времени на поиск медианы при использовании сортировки и без нее.
cProfile.run('main1()')
cProfile.run('main2()')
'''

# for main1()
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.002    0.002    3.556    3.556 <string>:1(<module>)
#    200001    0.107    0.000    0.151    0.000 random.py:237(_randbelow_with_getrandbits)
#    200001    0.126    0.000    0.277    0.000 random.py:290(randrange)
#    200001    0.066    0.000    0.343    0.000 random.py:334(randint)
#  400001/1    0.295    0.000    3.100    3.100 task7_3.py:15(array_sort)
#    200000    1.928    0.000    2.761    0.000 task7_3.py:25(array_merge)
#         1    0.001    0.001    3.554    3.554 task7_3.py:44(main)
#         1    0.088    0.088    0.453    0.453 task7_3.py:8(array_gen)
#         1    0.000    0.000    3.556    3.556 {built-in method builtins.exec}
#   8097946    0.597    0.000    0.597    0.000 {built-in method builtins.len}
#   3737876    0.302    0.000    0.302    0.000 {method 'append' of 'list' objects}
#    200001    0.018    0.000    0.018    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    254531    0.026    0.000    0.026    0.000 {method 'getrandbits' of '_random.Random' objects}
#
# for main2()
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    6.292    6.292 <string>:1(<module>)
#     20001    0.015    0.000    0.022    0.000 random.py:237(_randbelow_with_getrandbits)
#     20001    0.019    0.000    0.041    0.000 random.py:290(randrange)
#     20001    0.010    0.000    0.051    0.000 random.py:334(randint)
#         1    0.018    0.018    6.292    6.292 task7_3.py:48(main2)
#         1    0.014    0.014    0.068    0.068 task7_3.py:7(array_gen)
#         1    0.000    0.000    6.292    6.292 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     20002    5.141    0.000    5.141    0.000 {built-in method builtins.min}
#     30002    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
#     20001    0.003    0.000    0.003    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     25372    0.004    0.000    0.004    0.000 {method 'getrandbits' of '_random.Random' objects}
#     10001    1.064    0.000    1.064    0.000 {method 'remove' of 'list' objects}

