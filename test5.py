"""
Создать список чисел от 1 до 1 000 000, прибавляя к каждому элементу 10

В первом случае с помощью цикла

Во втором - используя ф-ци map и lambda

При первом способе количество памяти - 60.8 MiB
При втором - количество используемой памяти доходило до 99 MiB, но в конце кода
становилось таким же, как при использовании цикла.
При сокращении количества элементов на порядок отличия в памяти незначительны
(хотя, при выполнении map в обоих случаях наблюдается небольшой скачок
с последующим уменьшением)
При дальнейшем сокращении элементов отличий практически нет

"""
from memory_profiler import profile


@profile()
def func_2():
    """
    :return: список элементов плюс 10 c помощью цикла
    """
    lst_2 = []
    for i in range(1, 1000000):
        lst_2.append(i + 10)
    return lst_2


func_2()


@profile
def func_1():
    """
    :return: список элементов плюс 10, используя map  и  lambda
    """
    lst_1 = list(range(1, 1000000))
    lst_1 = list(map(lambda x: x + 10, lst_1))

    return lst_1


func_1()