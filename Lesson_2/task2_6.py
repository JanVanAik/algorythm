import random

answer = random.randint(0, 101)
counter = 1
user_answer = int(input('Угадайте число от 0 до 100: '))
while counter <= 10:
    if user_answer == answer:
        print(f'Верно! Правильный ответ: {answer}')
        break
    elif user_answer < answer:
        user_answer = int(input('Ошибка! Попробуйте еще раз, загаданное число больше вашего: '))
        counter += 1
    else:
        user_answer = int(input('Ошибка! Попробуйте еще раз, загаданное число меньше вашего: '))
        counter += 1
else:
    print(f'Вы не смогли угадать число. Правильный ответ был: {answer}')