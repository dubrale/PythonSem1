n = int(input('введите число: '))
fact = 1
if n > 0:
    for i in range(1,n+1):
        fact *= i
    print('факториал: ', fact)
else:
    if n == 0:
        print('факториал: 1')
    else:
        print('факториал - функция неотрицательного числа')