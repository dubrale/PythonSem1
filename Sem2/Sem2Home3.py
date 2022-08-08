print('Введите числа через запятую без пробела. Введенный ноль будет последним элементом сформированного списка')
num = list(map(int, input().split(',')))
num_new = []
n = len(num)

for i in range(0,num.index(0)+1):
    num_new.append(num[i])
print('Новый список: ', num_new)
max1 = max(num_new[0], num_new[1])
max2 = min(num_new[0], num_new[1])
n_new = len(num_new)
for i in range(2,n_new):
    if num_new[i] > max1:
        max2 = max1
        max1 = num_new[i]
    elif num_new[i] > max2 and max1 != num_new[i]:
        max2 = num_new[i]
    elif max1 == max2 and max2 != num_new[i]:
        max2 = num_new[i]
print('второе максимальное значение в списке, оканчивающемся на 0: ', max2)