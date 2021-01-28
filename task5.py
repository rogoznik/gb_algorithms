'''
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
'''

COUNT_ROW = 5
COUNT_COL = 4

matrix = []

print('Заполните матрицу натуральными числами до 9999')

for i in range(COUNT_ROW):
    matrix.append([])
    sum_col = 0
    for j in range(COUNT_COL - 1):
        matrix[i].append(int(input(f'Введите число [{i}][{j}]: ')))
        sum_col += matrix[i][j]
    matrix[i].append(sum_col)

for i in range(COUNT_ROW):
    for j in range(COUNT_COL - 1):
        print(f'{matrix[i][j]:>6}', end='')
    print(f'{matrix[i][j + 1]:>10}')
