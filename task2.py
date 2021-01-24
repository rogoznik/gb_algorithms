'''
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
'''


def get_summ(n, summ):
    if n < 10:
        summ += n
        return summ
    a = n % 10
    b = n // 10
    summ += a

    return get_summ(b, summ)


max_num = 0
max_sum = 0

while True:
    n = int(input('Введите натуральное число: '))
    if n < 1:
        print(f'Число с максимальной суммой: {max_num}')
        print(f'Сумма цифр: {max_sum}')
        break

    summ = get_summ(n, 0)

    if summ > max_sum:
        max_sum = summ
        max_num = n
