"""
 Реализовать функцию my_func(), которая принимает
 три позиционных аргумента, и возвращает сумму
 наибольших двух аргументов.
"""


def my_func_third(*args):
    """
    Исключение из суммы списка минимального элемента
    """
    my_lst = list(args)
    return sum(my_lst) - min(my_lst)
    


def my_func(arg_a, arg_b, arg_c):
    """
    функция без списка. Перебор возможных комбинаций
    """
    # print("Сумма двух наибольших аргументов(с помощью перебора): ")
    if arg_a <= arg_b <= arg_c:
        return arg_b + arg_c
    elif arg_a >= arg_b >= arg_c:
        return arg_b + arg_a
    elif arg_a < arg_b > arg_c:
        if arg_a > arg_c:
            return arg_b + arg_a
        else:
            return arg_b + arg_c
    else:
        return arg_a + arg_c


def my_func_second(arg_a, arg_b, arg_c):
    """
    создаём список из введённых аргументов, сортируем его в порядке возрастания
    и находим сумму последних двух элементов
    """
    my_lst = sorted([arg_a, arg_b, arg_c])
    #print(f"Сумма двух наибольших аргументов (функция sort): "
     #    f"{my_lst[1] + my_lst[2]}")
    return my_lst[1] + my_lst[2]

"""
try:
    arg_1 = float(input("Введите первый аргумент: "))
    arg_2 = float(input("Введите второй аргумент: "))
    arg_3 = float(input("Введите третий аргумент: "))
    print(my_func(arg_1, arg_2, arg_3))
    print(my_func_second(arg_1, arg_2, arg_3))
    print(my_func_third(arg_1, arg_2, arg_3))

except ValueError:
    print("Вы ввели текст или символ. Вводите числа")
"""



