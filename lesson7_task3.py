import random


def mediana(arr):
    med = None

    left_iter = 0
    right_iter = 0
    is_left = True
    is_right = False
    while True:
        count_left = 0
        count_right = 0
        count_copy = 0

        idx = -1

        if is_left:
            idx = left_iter
            left_iter += 1
            is_left = not is_left
            is_right = not is_right

        if is_right:
            idx = len(arr) - 1 - right_iter
            right_iter += 1
            is_left = not is_left
            is_right = not is_right

        med = arr[idx]
        for i in range(len(arr)):
            if i == idx:
                continue

            if arr[i] < med:
                count_left += 1
            elif arr[i] > med:
                count_right += 1
            else:
                count_copy += 1

        if count_copy == 0:
            if count_left == count_right:
                break
        else:
            if count_left + count_copy == count_right:
                break
            if count_right + count_copy == count_left:
                break

    return med


m = int(input('Введите натуральное число: '))

START_RAND = -1_000_000
END_RAND = 1_000_000

array = []

for _ in range(2 * m - 1):
    array.append(random.randint(START_RAND, END_RAND))

print(array)
print(f'Медиана массива: {mediana(array)}')
