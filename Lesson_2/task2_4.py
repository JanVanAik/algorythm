row = [1]
amount = int(input('Введите количество чисел последовательности: ' ))
for i in range(1, amount):
    row.append(float(-(row[i-1] / 2)))
print(row)
res = 0
for num in row:
    res += num
print(f'Сумма чисел равна: {res} ')