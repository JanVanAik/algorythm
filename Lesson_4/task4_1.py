import random
import cProfile


# task 9 from lesson 3
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


def print_matrix(column, row):
    matrix = matrix_gen(column, row)
    for k in range(row):
        for x in range(column):
            print(matrix[k][x], end=' ')
        print()


def main():
    column = 500
    row = 400
    print_matrix(column, row)
cProfile.run('main()')


# 1)Out for column = 50, row = 40
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.056    0.056 <string>:1(<module>)
#      1960    0.006    0.000    0.008    0.000 random.py:237(_randbelow_with_getrandbits)
#      1960    0.007    0.000    0.016    0.000 random.py:290(randrange)
#      1960    0.004    0.000    0.019    0.000 random.py:334(randint)
#         1    0.003    0.003    0.056    0.056 task4_1.py:20(print_matrix)
#         1    0.000    0.000    0.056    0.056 task4_1.py:28(main)
#         1    0.006    0.006    0.026    0.026 task4_1.py:8(matrix_gen)
#         1    0.000    0.000    0.056    0.056 {built-in method builtins.exec}
#      2040    0.026    0.000    0.026    0.000 {built-in method builtins.print}

# 2)Out for column = 500, row = 400
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    4.290    4.290 <string>:1(<module>)
#    199600    0.401    0.000    0.552    0.000 random.py:237(_randbelow_with_getrandbits)
#    199600    0.457    0.000    1.009    0.000 random.py:290(randrange)
#    199600    0.251    0.000    1.260    0.000 random.py:334(randint)
#         1    0.289    0.289    4.289    4.289 task4_1.py:20(print_matrix)
#         1    0.001    0.001    4.290    4.290 task4_1.py:28(main)
#         1    0.322    0.322    1.663    1.663 task4_1.py:8(matrix_gen)
#         1    0.001    0.001    4.290    4.290 {built-in method builtins.exec}
#    200400    2.337    0.000    2.337    0.000 {built-in method builtins.print}

# 3)Out for column = 5000, row = 4000
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1        0.000   0.000    164.671   164.671 < string >: 1( < module >)
# 19996000 10.135  0.000    14.157    0.000   random.py: 237(_randbelow_with_getrandbits)
# 19996000 11.954  0.000    26.112    0.000   random.py: 290(randrange)
# 19996000 6.071   0.000    32.183    0.000   random.py: 334(randint)
# 1        12.590  12.590   164.537   164.537 task4_1.py: 20(print_matrix)
# 1        0.135   0.135    164.671   164.671 task4_1.py: 28(main)
# 1        8.315   8.315    42.445    42.445  task4_1.py: 8(matrix_gen)
# 1        0.000   0.000    164.671   164.671 {built - in method builtins.exec}
# 20004000 109.501 0.000    109.501   0.000   {built - in method builtins.print}
#
