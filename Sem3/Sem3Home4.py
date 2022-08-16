n = int(input('введите число элементов: '))
fib_num = [0, 1]
for i in range(2,n):
    fib_num.append(fib_num[i-1]+fib_num[i-2])
for i in range(2,n):
    fib_num[i] = ((-1)**(i+1))*fib_num[i]
print('Последовательность: ', fib_num)