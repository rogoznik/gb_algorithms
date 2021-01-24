'''
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
'''


n = int(input('Введите натурально число: '))

b = n
revers = ''

while True:
    if b < 10:
        revers += str(b)
        break

    a = b % 10
    b = b // 10

    if revers == '' and a != 0:
        revers += str(a)
    elif revers != '':
        revers += str(a)

print(f'Число наоборот: {revers}')
