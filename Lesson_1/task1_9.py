num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))

# Здесь применяется функция sort и выводится второй элемент
if num_1 >= num_2 and num_1 >= num_3: # Если первое число самое большое - выбираем из 2,3
    if num_2 >= num_3:
        print(num_2)
    else:
        print(num_3)
elif num_1 < num_3 or num_1 < num_2:  #Если первое число число  самое маленькое - выбираем из 2 и 3
    if num_2 > num_3:
        print(num_3)
    else:
        print(num_2)
else:  # Иначе 1 число - среднее
    print(num_1)
