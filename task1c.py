from timeit import timeit
from cProfile import run


def main(array):
    max_num = 0
    max_sum = 0

    i = 0
    while i < len(array):
        num = array[i]
        summ = 0

        if num < 10:
            summ += num
            i += 1
            continue

        for c in str(i):
            summ += int(c)

        if summ > max_sum:
            max_sum = summ
            max_num = array[i]
        
        i += 1
    return max_num, max_num

n = 1_000
array = [i for i in range(1, n + 1)]
print(timeit('main(array)',  number=100, globals=globals()))    # 0.05967424700065749 
n = 10_000
array = [i for i in range(1, n + 1)]
print(timeit('main(array)',  number=100, globals=globals()))    # 0.7249569760024315
n = 100_000
array = [i for i in range(1, n + 1)]
print(timeit('main(array)',  number=100, globals=globals()))    # 7.868347547002486
n = 1_000_000
array = [i for i in range(1, n + 1)]
print(timeit('main(array)',  number=100, globals=globals()))    # 93.22402546699595

n = 1_000
array = [i for i in range(1, n + 1)]
run('main(array)')
'''
         1005 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 task1c.py:5(main)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
     1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
n = 10_000
array = [i for i in range(1, n + 1)]
run('main(array)')
'''
         10005 function calls in 0.008 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.008    0.008 <string>:1(<module>)
        1    0.008    0.008    0.008    0.008 task1c.py:5(main)
        1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
    10001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
n = 100_000
array = [i for i in range(1, n + 1)]
run('main(array)')
'''
         100005 function calls in 0.094 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.094    0.094 <string>:1(<module>)
        1    0.088    0.088    0.094    0.094 task1c.py:5(main)
        1    0.000    0.000    0.094    0.094 {built-in method builtins.exec}
   100001    0.006    0.000    0.006    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
n = 1_000_000
array = [i for i in range(1, n + 1)]
run('main(array)')
'''
         1000005 function calls in 1.007 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.007    1.007 <string>:1(<module>)
        1    0.944    0.944    1.007    1.007 task1c.py:5(main)
        1    0.000    0.000    1.007    1.007 {built-in method builtins.exec}
  1000001    0.063    0.000    0.063    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''