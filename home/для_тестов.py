def triangle(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        print('Прямоугольный')
    elif a ** 2 + c ** 2 == b ** 2:
        print('Прямоугольный')
    else:
        if c ** 2 + b ** 2 == a ** 2:
            print('Прямоугольный')
        else:
            print('Не прямоугольный')


print(triangle(3, 22, 3))
