import random

column = 5
row = 4
matrix = []
for i in range(row):
    m_string = []
    for j in range(column - 1):
        num = random.randint(0, 100)
        m_string.append(num)
    m_string.append(sum(m_string))
    matrix.append(m_string)

for k in range(row):
    for x in range(column):
        print(matrix[k][x], end=' ')
    print()

for element in range(0, column - 1):
    minimum = 100  # 100 - максимальный размер генерируемого числа
    for ind in range(0, row):
        if matrix[ind][element] < minimum:
            minimum = matrix[ind][element]
    print(f'В {element + 1} стобце минимум равен {minimum}')
