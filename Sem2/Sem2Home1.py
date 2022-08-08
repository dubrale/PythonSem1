num = str(input('введите число: '))
num_final =num.replace(",","")
sum = 0
for digit in num_final:
    digit = int(digit)
    sum += digit
print(sum)