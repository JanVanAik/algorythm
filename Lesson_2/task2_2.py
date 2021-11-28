num = input('Введите число: ')
odd = []
even = []
for letter in num:
    if int(letter) % 2 == 0:
        even += letter
    else:
        odd += letter

print(f'Нечетные: {odd},\nЧетные: {even}')