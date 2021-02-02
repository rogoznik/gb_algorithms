'''
С использованием решета Эратосфена
Функция возвращает n-е простое число
'''

from timeit import timeit
from cProfile import run


def main(n):
    len_ = n * 20

    sieve = [i for i in range(len_)]
    sieve[1] = 0

    k = 0
    for i in range(2, len_):
        if sieve[i] != 0:
            k += 1
            if k == n:
                break
            j = i + i
            while j < len_:
                sieve[j] = 0
                j += i

    return sieve[i]




# print(timeit('main(100)',  number=100, globals=globals()))          # 0.030306854998343624
# print(timeit('main(1_000)',  number=100, globals=globals()))        # 0.3590633620042354
# print(timeit('main(10_000)',  number=100, globals=globals()))       # 4.3490311360001215
# print(timeit('main(100_000)',  number=100, globals=globals()))      # 55.88570631900075
# print(timeit('main(1_000_000)',  number=100, globals=globals()))    # 685.1814794239981

run('main(100)')
'''
         5 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task2a.py:10(main)
        1    0.000    0.000    0.000    0.000 task2a.py:13(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
run('main(1_000)')
'''
         5 function calls in 0.004 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
        1    0.003    0.003    0.004    0.004 task2a.py:10(main)
        1    0.001    0.001    0.001    0.001 task2a.py:13(<listcomp>)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
run('main(10_000)')
'''
         5 function calls in 0.044 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.044    0.044 <string>:1(<module>)
        1    0.038    0.038    0.043    0.043 task2a.py:10(main)
        1    0.005    0.005    0.005    0.005 task2a.py:13(<listcomp>)
        1    0.000    0.000    0.044    0.044 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
run('main(100_000)')
'''
         5 function calls in 0.593 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.012    0.012    0.593    0.593 <string>:1(<module>)
        1    0.528    0.528    0.581    0.581 task2a.py:10(main)
        1    0.053    0.053    0.053    0.053 task2a.py:13(<listcomp>)
        1    0.000    0.000    0.593    0.593 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
run('main(1_000_000)')
'''
         5 function calls in 6.707 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.101    0.101    6.707    6.707 <string>:1(<module>)
        1    6.078    6.078    6.606    6.606 task2a.py:10(main)
        1    0.527    0.527    0.527    0.527 task2a.py:13(<listcomp>)
        1    0.000    0.000    6.707    6.707 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''