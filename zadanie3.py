from random import randint

def change(a):
    for i in range(int(len(a) / 2)):
        tempA = a[i]
        a[i] = a[len(a) - 1 - i]
        a[len(a) - i - 1] = tempA
    print(a)
    return a


print("Введите значение С от 1 до 10:")
c = int(input())
print("Введите значения M(столбцов) и N(строк):")
m = int(input())
n = int(input())

if (n % 2 == 0) and (n > 1) and (m > 1):
    a = [[randint(1, 10) for j in range(m)] for i in range(n)]
    print(a)

    flag = 0
    for i in range(int(len(a))):
        if a[i][m-1] == c:
            change(a)
            flag = 1
            break
    lastI = 0
    if flag == 0:
        for i in range(int(len(a))):
            if a[i][m-1] >= c:
                lastI = i
        if lastI == 0:
            print("В последнем столбце нет элементов больше С")
        else:
            print("В " + str(lastI) + " строке находится последний элемент больше С. (нумерация строк с идет с нулевой)")
