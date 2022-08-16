my_n = input('введите число знаков после запятой: ')
n = "%." + my_n + "f"
sum = 1
my_pi = 1
for i in range(1,1000000):
    sum += ((-1)**(i))/(2*i+1)
my_pi = sum*4
print('Pi: ', n % my_pi)