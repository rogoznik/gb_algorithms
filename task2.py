from collections import deque


def hex_to_dec(hex_):
    dict_transform = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    base = 16
    res = 0
    power = 0
    for i in range(len(hex_)):
        res += int(dict_transform[hex_.pop().upper()]) * (base ** power)
        power += 1

    return res


def dec_to_hex(dec):
    dict_transform = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    base = 16
    res = deque()
    while True:
        q = dec // base
        res.append(dict_transform[dec % base])
        if q < base:
            break
        dec = q
    res.append(dict_transform[q])
    res.reverse()
    if res[0] == '0':
        res.popleft()
    return res


operands = dict()

print('Введите целые положительные числа в шестнадцетиричной системе счисления')
operands['a'] = deque(input('Первое число: '))
operands['b'] = deque(input('Второе число: '))

a = hex_to_dec(operands['a'])
b = hex_to_dec(operands['b'])

print(f'Сумма: {dec_to_hex(a + b)}')
print(f'Произведение: {dec_to_hex(a * b)}')
