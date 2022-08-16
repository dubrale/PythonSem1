from random import randint
n = int(input('введите степень многочлена: '))
polynom = ''
for i in range(0,n+1):
    polynom += (str(randint(1, 20))+'x^'+str(n-i)+' + ')
print(polynom[:-6])