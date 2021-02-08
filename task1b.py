import sys

n = int(input('Введите натурально число: '))

b = n
revers = 0

while True:
    if b < 10:
        revers += b
        break

    a = b % 10
    b = b // 10

    revers += a
    revers *= 10

print(f'Число наоборот: {revers}')

sum_size = 0
sum_size += sys.getsizeof(n)
sum_size += sys.getsizeof(b)
sum_size += sys.getsizeof(revers)
sum_size += 28  # кол-во памяти, которое занимает переменная a во время работы цикла

print(f'Переменные занимают: {sum_size}')  # если ввести число 123, то sum_size = 112
