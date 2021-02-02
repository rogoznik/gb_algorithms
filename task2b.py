'''
Алгоритм перебора делителей
'''

from timeit import timeit
from cProfile import run


n = 1_000 # какое по счету простое число нужно найти

def main(n):
    len_ = n * 20

# array = [i for i in range(2, len_)]
    k = 0


# for i in range(2, len_):
#     d = 2
#     j = 0

#     while d * d <= i and j != 1:
#         if i % d == 0:
#             j = 1
#         d += 1

#     if j == 0:
#         if k == n:
#             break
#         k += 1

    i = 2
    while k != n and i <= len_:
        d = 2
        j = 0

        while d * d <= i and j != 1:
            if i % d == 0:
                j = 1
            d += 1

        if j == 0:
            k += 1
        
        i += 1
    
    return i - 1


# print(timeit('main(100)',  number=100, globals=globals()))          # 0.029524344005039893
# print(timeit('main(1_000)',  number=100, globals=globals()))        # 0.9634392830048455
# print(timeit('main(10_000)',  number=100, globals=globals()))       # 32.62993957899744
# print(timeit('main(100_000)',  number=100, globals=globals()))      # 1340.7759982839998
# print(timeit('main(1_000_000)',  number=100, globals=globals()))    # не дождался окончания(ждал примерно 10 часов)

run('main(100)')
'''
         4 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 task2b.py:11(main)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
run('main(1_000)')
'''
         4 function calls in 0.010 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.010    0.010 <string>:1(<module>)
        1    0.010    0.010    0.010    0.010 task2b.py:11(main)
        1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
run('main(10_000)')
'''
         4 function calls in 0.316 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.316    0.316 <string>:1(<module>)
        1    0.316    0.316    0.316    0.316 task2b.py:11(main)
        1    0.000    0.000    0.316    0.316 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
run('main(100_000)')
'''
         4 function calls in 10.950 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   10.950   10.950 <string>:1(<module>)
        1   10.950   10.950   10.950   10.950 task2b.py:11(main)
        1    0.000    0.000   10.950   10.950 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
run('main(1_000_000)')
'''
         4 function calls in 371.530 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000  371.530  371.530 <string>:1(<module>)
        1  371.530  371.530  371.530  371.530 task2b.py:11(main)
        1    0.000    0.000  371.530  371.530 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
