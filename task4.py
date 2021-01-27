'''
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
(индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
'''

import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# Вариант с генератором
array_idxs = [i for i, num in enumerate(array) if num % 2 == 0 and num != 0]

print(array_idxs)

# Вариант с циклом
array_idxs = []
for i, num in enumerate(array):
    if num % 2 == 0 and num != 0:
        array_idxs.append(i)

print(array_idxs)
