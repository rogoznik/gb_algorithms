'''
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''

START_NUM = 2
END_NUM = 99
START_DIV = 2
END_DIV = 9

array_nums = [i for i in range(START_NUM, END_NUM + 1)]
array_divs = [i for i in range(START_DIV, END_DIV + 1)]
array_counts = [0 for i in range(len(array_divs))]

for num in array_nums:
    for i, div in enumerate(array_divs):
        if num % div == 0:
            array_counts[i] += 1

for i in range(0, 8):
    print(f'{array_divs[i]} - {array_counts[i]}')
