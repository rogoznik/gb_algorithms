'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_num = array[0]
max_num = array[0]
idx_min_num = 0
idx_max_num = 0

for i, num in enumerate(array):
    if num > max_num:
        max_num = num
        idx_max_num = i
    if num < min_num:
        min_num = num
        idx_min_num = i

array[idx_min_num], array[idx_max_num] = array[idx_max_num], array[idx_min_num]

print(f'{min_num=}, {idx_min_num=}')
print(f'{max_num=}, {idx_max_num=}')
print(array)
