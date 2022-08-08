print('введите день недели:')
a = int(input())
if a > 0 and a < 8:
    if a % 2 == 0:
        print ('четный день недели')
    else:
        print ('нечетный день недели')
else:
    print ('дней недели семь')
