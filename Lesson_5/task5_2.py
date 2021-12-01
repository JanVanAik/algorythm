def convert_base(num, to_base=16, from_base=10):
    # first convert to decimal number
    n = int(num, from_base) if isinstance(num, str) else num
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        n, m = divmod(n, to_base)
        res += alphabet[m]
    return res[::-1]
#модуля по конвертации не нашел, взял со stackoverflow

expression = input('Введите через запятую два числа и знак операции(+, *): ').replace(' ', '').split(',')
num1 = [i for i in expression[0]]
num2 = [i for i in expression[1]]
num1 = num1[::-1]
num2 = num2[::-1]
sign = expression[2]
sum = []
while len(num1) != len(num2):
    if len(num1) > len(num2):
        num2.append('0')
    else:
        num1.append('0')

for i in range(len(num1)):
    sum.append(0)

if sign == '+':
    leftovers = 0
    for i in range(len(sum)):
        if leftovers == 0:
            sum[i] = convert_base(int(num1[i], 16) + int(num2[i], 16))
            if len(sum[i]) > 1:
                leftovers = sum[i][0]
                sum[i] = sum[i][1]
        elif leftovers != 0:
            sum[i] = convert_base(int(num1[i], 16) + int(num2[i], 16) + int(leftovers, 16))
            if len(sum[i]) > 1:
                leftovers = sum[i][0]
                sum[i] = sum[i][1]
    sum = sum[::-1]
    print(sum)