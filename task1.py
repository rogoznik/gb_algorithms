'''
ссылка на схемы: https://drive.google.com/file/d/1uGsdO2NkdQidpayB3ntSnV_4kU66qgXD/view?usp=sharing

Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
'''

a = int(input('Введите трехзначное число: '))

c1 = a // 100
c2 = a % 100 // 10
c3 = a % 10

summa = c1 + c2 + c3
composition = c1 * c2 * c3

print(f'сумма цифр = {summa}')
print(f'произведение цифр = {composition}')
