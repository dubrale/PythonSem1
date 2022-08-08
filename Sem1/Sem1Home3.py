print('введите координату Х:')
x = int(input())
print('введите координату Y:')
y = int(input())
if x == 0 or y == 0:
    print('X или Y не должны равняться нулю')
else:
    if x > 0 and y > 0:
        print('1-я четверть')
    else:
        if x < 0 and y > 0:    
            print('2-я четверть')
        else:
            if x < 0 and y < 0:    
                print('3-я четверть')
            else:
                if x > 0 and y < 0:    
                    print('4-я четверть')