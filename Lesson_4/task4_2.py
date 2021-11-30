# https://en.m.wikipedia.org/wiki/Prime-counting_function
# x/log(x)
import math


def eratosthenes(n, pos):
    sieve = list(range(n + 1))
    sieve[1] = 0
    counter = 0
    for i in sieve:
        if i > 1:
            counter += 1
            if counter == pos:
                return i
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve, counter



number = int(input('Введите номер простого числа: '))
amount = 10
while number > amount/math.log(amount):
    amount += 100
print(amount)
print(eratosthenes(amount, number))

