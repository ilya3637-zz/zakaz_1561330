import math as t

MAX_COUNT = 2500
x = 0.5
Func = 0.0
Eps = 0.0
X = [-0.98, -0.5, 0.1, 0.5, 0.95]
i = 0
s_i = 0.0
Sums = 0.0
j = 0
z = 0
zs = ''
format_s = ''

print('Вычисление функции разложением ее в ряд.\n\n')
Eps = float(input('Введите точность EPS: '))
print('Eps = {0:e}'.format(Eps))
Func = 3 * t.exp((1/3)*t.log(1+x)) - 3
print('Контрольное значение функции = {0:9.6f}'.format(Func))
z = t.ceil(t.fabs(t.log(Eps)/t.log(10))) + 1
zs = str(z)
print('N |        X |     S(X) |  K |     F(X) ||S(X)-F(X)|')
print('================================================================================')

for j in range(len(X)):
    x = X[j]
    i = 1
    s_i = x
    Sums = s_i
    while (t.fabs(s_i) >= Eps) and (i != MAX_COUNT):
        i += 1
        s_i = (-s_i) * (3 * i - 4) * x / (3 * i)
        Sums = Sums + s_i

    format_s = '{0:2d}|{1:10.' + zs + 'f}|{2:10.' + zs + 'f}|{3:4d}|{4:10.' + zs + 'f}|{5:10.' + zs + 'f}|'
    print(format_s.format(j, X[j], Sums, i, Func, t.fabs(Sums - Func)))


