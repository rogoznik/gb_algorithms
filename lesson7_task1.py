import random


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


START_RAND = -100
END_RAND = 100

array = []

for _ in range(10):
    array.append(random.randint(START_RAND, END_RAND - 1))

print(array)
bubble_sort(array)
print(array)

