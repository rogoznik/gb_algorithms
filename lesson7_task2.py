'''
Если правильно понял - реализованный мной алгоритм называется "Естественное неймановское слияние"
Не исключаю что что-то упустил, но алгоритм, вроде, работает :)))
'''

import random


def merge_sort(arr):
    b = []
    c = []
    while len(b) < len(arr):
        b.clear()
        c.clear()
        is_b = True
        is_c = False
        b.append(arr[0])
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                is_b = not is_b
                is_c = not is_c

            if is_b:
                b.append(arr[i])
            if is_c:
                c.append(arr[i])

        ia = 0
        ib = 0
        ic = 0

        while ib < len(b) and ic < len(c):
            if b[ib] < c[ic]:
                arr[ia] = b[ib]
                ib += 1
            else:
                arr[ia] = c[ic]
                ic += 1
            ia += 1

        if ib >= len(b):
            for k in range(ia, len(arr)):
                arr[k] = c[ic]
                ic += 1
        elif ic >= len(c):
            for k in range(ia, len(arr)):
                arr[k] = b[ib]
                ib += 1


START_RAND = 0
END_RAND = 50

array = []

for _ in range(10):
    array.append(random.randint(START_RAND, END_RAND - 1))

print(array)
merge_sort(array)
print(array)
