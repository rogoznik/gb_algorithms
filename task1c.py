import sys
from collections import deque


n = deque(input('Введите натурально число: '))
n.reverse()
print(''.join(n))

print(f'Переменные занимают: {sys.getsizeof(n)}')  # если ввести число 123, то sys.getsizeof(n) = 624
