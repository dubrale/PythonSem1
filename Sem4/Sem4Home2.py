my_n = int(input('введите число, для которого хотите найти простые делители: '))
def prime_factors(n):
    i = 2
    pr_fact = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            pr_fact.append(i)
    if n > 1:
        pr_fact.append(n)
    return pr_fact
def result(original_list):
    res_list = [] 
    for i in original_list: 
        if i not in res_list: 
            res_list.append(i)
    return res_list
print('Простые делители числа', my_n, ': ', result(prime_factors(my_n)))
