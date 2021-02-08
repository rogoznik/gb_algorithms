'''
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.

Python 3.8.5 64-bit
OS Linux 64-bit

Вывод:
Очевидно вариант решения в файле task1b.py лучше, т.к. использует мешьше памяти. Думаю связано с тем что используется
только простой тип данных int
'''

import sys


n = int(input('Введите натурально число: '))

b = n
revers = ''

while True:
    if b < 10:
        break

    a = b % 10
    b = b // 10
    if revers == '' and a != 0:
        revers += str(a)
    elif revers != '':
        revers += str(a)

print(f'Число наоборот: {revers}')

sum_size = 0
sum_size += sys.getsizeof(n)
sum_size += sys.getsizeof(b)
sum_size += sys.getsizeof(revers)
sum_size += 28  # кол-во памяти, которое занимает переменная a во время работы цикла

print(f'Переменные занимают: {sum_size}')  # если ввести число 123, то sum_size = 135
