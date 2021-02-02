from timeit import timeit
from cProfile import run


def main(array):
    max_num = 0
    max_sum = 0

    i = 0
    while i < len(array):
        num = array[i]
        summ = 0
        while True:
            if num < 10:
                summ += num
                break
            a = num % 10
            num = num // 10
            summ += a

        if summ > max_sum:
            max_sum = summ
            max_num = array[i]
        
        i += 1
    return max_num, max_num

n = 1_000
array = [i for i in range(1, n + 1)]
print(timeit('main(array)',  number=100, globals=globals()))    # 0.029176409996580333 
n = 10_000
array = [i for i in range(1, n + 1)]
print(timeit('main(array)',  number=100, globals=globals()))    #  0.36032617899763864
n = 100_000
array = [i for i in range(1, n + 1)]
print(timeit('main(array)',  number=100, globals=globals()))    #  4.368767211999511
n = 1_000_000
array = [i for i in range(1, n + 1)]
print(timeit('main(array)',  number=100, globals=globals()))    # 51.58887921900168

n = 1_000
array = [i for i in range(1, n + 1)]
run('main(array)')
'''
         1005 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task1b.py:5(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
     1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
n = 10_000
array = [i for i in range(1, n + 1)]
run('main(array)')
'''
         10005 function calls in 0.005 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
        1    0.004    0.004    0.005    0.005 task1b.py:5(main)
        1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
    10001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
n = 100_000
array = [i for i in range(1, n + 1)]
run('main(array)')
'''
         100005 function calls in 0.053 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.053    0.053 <string>:1(<module>)
        1    0.048    0.048    0.053    0.053 task1b.py:5(main)
        1    0.000    0.000    0.053    0.053 {built-in method builtins.exec}
   100001    0.005    0.000    0.005    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
n = 1_000_000
array = [i for i in range(1, n + 1)]
run('main(array)')
'''
         1000005 function calls in 0.603 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.603    0.603 <string>:1(<module>)
        1    0.555    0.555    0.603    0.603 task1b.py:5(main)
        1    0.000    0.000    0.603    0.603 {built-in method builtins.exec}
  1000001    0.048    0.000    0.048    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''