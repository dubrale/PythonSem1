from math import sqrt


print('введите координату первой точки через запятую без пробела:')
x1, y1 = map(int, input().split(','))
print('введите координату второй точки через запятую без пробела:')
x2, y2 = map(int, input().split(','))
s = sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
print(s)