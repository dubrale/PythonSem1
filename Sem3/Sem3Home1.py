print('Введите числа через запятую без пробела')
num = list(map(int, input().split(',')))
sum = 0
for i in range(1,len(num),2):
    sum += num[i]   
print('Сумма элементов на нечетных позициях: ', sum)
