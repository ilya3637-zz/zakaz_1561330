import math

triangles = []
a = float(1)
b = float(1)
c = float(1)
max = 0
number = 0
iNumber = 0

while a != 0:
    print("Введите три значения сторон треугольника или букву для результата:")
    try:
        number = number + 1
        a = int(input())
        b = int(input())
        c = int(input())
        p = (a + b + c) / 2
        r = (math.sqrt(p * (p - a) * (p - b) * (p - c))) / p
        triangles.append(r)
        if (r > max):
            max = r
            iNumber = number
    except ValueError or TypeError:
        a = 0
        b = 0
        c = 0

print("\nВы ввели неправильное соотнешение сторон или букву.")
print("Максимальный радиус вписанной окружности полуился у " + str(iNumber) + " треугольника и равен " + str(max))
