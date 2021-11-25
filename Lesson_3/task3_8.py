column = 5
row = 4
matrix = []
for i in range(row):
    m_string = []
    for j in range(column-1):
        num = int(input(f'Введите {j+1} элемент {i+1} строки: '))
        m_string.append(num)
    m_string.append(sum(m_string))
    matrix.append(m_string)

for k in range(row):
    for x in range(column):
        print(matrix[k][x], end=' ')
    print()
