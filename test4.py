"""
Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти,
оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали
и чего удалось добиться

Создать список чисел от 100 до 500 000 из чётных элементов
Необходимо получить результат вычисления суммы
 всех элементов списка.
 В первом случае вычисления с помощью ф-ции reduce
 Во втором - с помощью цикла
 В обоих случаях памяти выделяется одинаково


"""
from memory_profiler import profile

from functools import reduce


@profile()
def func_1():
    my_lst = [i for i in range(100, 500000) if i % 2 == 0]

    my_res_sum = reduce((lambda x, y: x + y), my_lst)

    print(my_res_sum)


func_1()


@profile()
def func():
    my_lst = [i for i in range(100, 500000) if i % 2 == 0]

    my_res_sum = 0
    for j in my_lst:
        my_res_sum += j

    print(my_res_sum)


func()