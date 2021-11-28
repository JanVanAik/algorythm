num = input('Введите число: ')
num_reverse = []
for number in num:
    num_reverse.append(number)
num_reverse.reverse()
print(''.join(num_reverse))
