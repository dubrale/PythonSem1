print('Введите числа через запятую без пробела')
num = list(map(int, input().split(',')))
def result(original_list):
    res_list = [] 
    for i in original_list: 
        if i not in res_list: 
            res_list.append(i)
    return res_list
print('Список без повторов: ', result(num))