'''
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. 
Вывести на экран это число и сумму его цифр.

1a. Решение рекурсией
1b. Решение циклом
1c. Цикл с использованием строки

Вывод:
Алгоритм решения b работает быстрей. 
Думаю это связано с тем, что при использовании рекурсии 
дополнительно тратиться время на постановку/снятие функции в/из стек(а) вызовов.
А при использовании строк, думаю затрачивается время на преобразония из числа в строку и обратно.
'''

from timeit import timeit
from cProfile import run


def get_summ(n, summ):
    if n < 10:
        summ += n
        return summ
    a = n % 10
    b = n // 10
    summ += a

    return get_summ(b, summ)

def main(array):
    max_num = 0
    max_sum = 0

    i = 0
    while i < len(array):
        summ = get_summ(array[i], 0)

        if summ > max_sum:
            max_sum = summ
            max_num = array[i]
        
        i += 1
    return max_num, max_num


n = 1_000
array = [i for i in range(1, n + 1)]
print(timeit('main(array)',  number=100, globals=globals()))    # 0.04457754900067812 
n = 10_000
array = [i for i in range(1, n + 1)]
print(timeit('main(array)',  number=100, globals=globals()))    #  0.514154126001813
n = 100_000
array = [i for i in range(1, n + 1)]
print(timeit('main(array)',  number=100, globals=globals()))    #  6.534911648996058
n = 1_000_000
array = [i for i in range(1, n + 1)]
print(timeit('main(array)',  number=100, globals=globals()))    # 77.54927268400206


n = 1_000
array = [i for i in range(1, n + 1)]
run('main(array)')
'''
         3898 function calls (2005 primitive calls) in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
2893/1000    0.000    0.000    0.000    0.000 task1a.py:15(get_summ)
        1    0.000    0.000    0.001    0.001 task1a.py:25(main)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
     1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
n = 10_000
array = [i for i in range(1, n + 1)]
run('main(array)')
'''
         48899 function calls (20005 primitive calls) in 0.011 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.011    0.011 <string>:1(<module>)
38894/10000    0.007    0.000    0.007    0.000 task1a.py:15(get_summ)
        1    0.003    0.003    0.011    0.011 task1a.py:25(main)
        1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
    10001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
n = 100_000
array = [i for i in range(1, n + 1)]
run('main(array)')
'''
         588900 function calls (200005 primitive calls) in 0.126 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.126    0.126 <string>:1(<module>)
488895/100000    0.095    0.000    0.095    0.000 task1a.py:15(get_summ)
        1    0.026    0.026    0.126    0.126 task1a.py:25(main)
        1    0.000    0.000    0.126    0.126 {built-in method builtins.exec}
   100001    0.005    0.000    0.005    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
n = 1_000_000
array = [i for i in range(1, n + 1)]
run('main(array)')
'''
         6888901 function calls (2000005 primitive calls) in 1.474 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.474    1.474 <string>:1(<module>)
5888896/1000000    1.166    0.000    1.166    0.000 task1a.py:15(get_summ)
        1    0.258    0.258    1.474    1.474 task1a.py:25(main)
        1    0.000    0.000    1.474    1.474 {built-in method builtins.exec}
  1000001    0.050    0.000    0.050    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''