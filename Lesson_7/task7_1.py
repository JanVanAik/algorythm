from random import randint
import cProfile

from random import randint


def bubble_sort(array):
    const = len(array)
    n = 1
    while n < const:
        for i in range(const - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array


def array_gen(start, end, amount):
    array = []
    for i in range(amount):
        array.append(randint(start, end))
    return array


def main():
    my_array = array_gen(-100, 100, 10000)
    print(my_array)
    print(bubble_sort(my_array))


cProfile.run('main()')

'''
len != const, 10 000 numbers

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    9.161    9.161 <string>:1(<module>)
    10000    0.008    0.000    0.011    0.000 random.py:237(_randbelow_with_getrandbits)
    10000    0.009    0.000    0.021    0.000 random.py:290(randrange)
    10000    0.005    0.000    0.026    0.000 random.py:334(randint)
        1    0.007    0.007    0.034    0.034 task7_1.py:18(array_gen)
        1    0.000    0.000    9.161    9.161 task7_1.py:25(main)
        1    9.120    9.120    9.124    9.124 task7_1.py:7(bubble_sort)  
        1    0.000    0.000    9.161    9.161 {built-in method builtins.exec}
    19999    0.004    0.000    0.004    0.000 {built-in method builtins.len}
        2    0.002    0.001    0.002    0.001 {built-in method builtins.print}
    10000    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12934    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}

len = const, 10 000 numbers

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    8.942    8.942 <string>:1(<module>)
    10000    0.008    0.000    0.012    0.000 random.py:237(_randbelow_with_getrandbits)
    10000    0.010    0.000    0.023    0.000 random.py:290(randrange)
    10000    0.005    0.000    0.028    0.000 random.py:334(randint)
        1    0.008    0.008    0.038    0.038 task7_1.py:18(array_gen)
        1    0.000    0.000    8.942    8.942 task7_1.py:25(main)
        1    8.901    8.901    8.901    8.901 task7_1.py:7(bubble_sort)
        1    0.000    0.000    8.942    8.942 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        2    0.003    0.001    0.003    0.001 {built-in method builtins.print}
    10000    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12793    0.003    0.000    0.003    0.000 {method 'getrandbits' of '_random.Random' objects}
'''

'''
         1    9.120    9.120    9.124    9.124 task7_1.py:7(bubble_sort)  
        
         1    8.901    8.901    8.901    8.901 task7_1.py:7(bubble_sort)
         
Как можем заметить - выигрыш по времени весьма незначителен
'''