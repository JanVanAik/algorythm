
num = int(input('Введите число: '))
left = 0
right = num * (num + 1 )/2
for i in range(1, num+1):
    left +=i
if left == right:
    print('Верно')
else:
    print('Равенство неверно')
