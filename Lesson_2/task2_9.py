user_answer = input('Введите числа через запятую: ').replace(' ', '').split(',')
max = 0
for i in user_answer:
    sum = 0
    for num in i:
        sum += int(num)
    if sum > max:
        max = sum
        answer = (i, max)
print(f'Самое большое число и сумма его цифр: {answer}')
