print('Введите числа через запятую без пробела')
num = list(map(int, input().split(',')))
num_new = []
for i in range(0,(len(num)+1)//2):  
    num_new.append(num[i]*num[-i-1])
print('Новый список: ', num_new)