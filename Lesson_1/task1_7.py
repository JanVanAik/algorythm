side_str = input('Введите длины сторон треугольников через запятую: ').split(',')
sides = [int(i) for i in side_str]
sides.sort()
if sides[0]+sides[1] > sides[2]:
    if sides[0] == sides[1] and sides[0] == sides[2]:
        print('Треугольник составить можно, он равносторонний')
    elif sides[0] == sides[1]:
        print('Треугольник составить можно, он равнобедренный')
    elif sides[0]**2 + sides[1]**2 == sides[2] ** 2:
        print('Треугольник составить можно, он прямоугольный')
    else:
        print('Треугольник составить можно. Он максимально обычный')
else:
    print('Треугольник составить нельзя')