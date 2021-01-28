'''
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
'''


import random

SIZE = 100
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_negative_num = MIN_ITEM

for i, item in enumerate(array):
    if item == -1:
        max_negative_num = item
        idx = i
        break

    if item < 0:
        if item > max_negative_num:
            max_negative_num = item
            idx = i

print(f'Максимальное отрицательное число: {max_negative_num}, его индекс в массиве: {idx}')