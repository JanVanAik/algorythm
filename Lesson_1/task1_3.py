first_spot = input('Введите координаты x и y первой точки через запятую: ').split(',')
second_spot = input('Введите координаты x и y второй точки через запятую: ').split(',')
# y=  kx +b - вид, который нам нужен. Формула x-x1/x2-x1 = y-y1/y2-y1
dot_1 = [int(i) for i in first_spot]
dot_2 = [int(i) for i in second_spot]
x2_minus_x1 = dot_2[0] - dot_1[0]
y2_minus_y1 = dot_2[1] - dot_1[1]

print(f'Уравнение прямой, проходящей через эти точки: '
      f'y={y2_minus_y1/x2_minus_x1}x + {dot_1[1] - dot_1[0]* y2_minus_y1/x2_minus_x1 }')
