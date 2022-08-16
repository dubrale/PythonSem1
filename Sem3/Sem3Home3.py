print('Введите вещественные числа через запятую без пробела(не больше 5 знаков после запятой)')
num = list(map(float, input().split(',')))
num_new = []
diff = 0
for i in range(0,len(num)):
    num_new.append(abs(round(num[i]%1,5)))
print('Список дробных частей чисел: ', num_new)
diff = max(num_new) - min(num_new)
print('Разноть макcимального и минимального элементов списка дробных частей числел: ', diff)
