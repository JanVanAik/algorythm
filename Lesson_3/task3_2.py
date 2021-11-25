mass = input('Введите числа через запятую: ')
mass = mass.replace(' ', '').split(',')
print([index for index, val in enumerate(mass) if int(val) % 2 == 0])
