# Если хотим написать вывод обратного отсчета 3 ... 2 ... 1
# в рекурсивном виде
def count_down(i):
    print(i)
    count_down(i - 1)


# Функция выполняется бесконечно
''' count_down(5) '''


# Добавляем базовый случай в функцию
def count_down1(i):
    print(i)
    if i <= 0:  # Базовый случай
        return
    else:  # Рекурсивный случай
        count_down1(i - 1)


'''count_down1(5)'''


# Рекурсивная функция по вычислению факториала
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


'''print(fact(5))'''


# Рекурсивная функция по расчету суммы элементов списка
def sum_arr(arr: list):
    if len(arr) == 0:
        return 0
    else:
        return arr.pop(0) + sum_arr(arr)


print(sum_arr([1, 10, 10, 213, 13]))


# функция по подсчету элементов в списке
def len_arr(arr: list):
    if len(arr) == 0:
        return 0
    else:
        arr.pop(-1)
        return 1 + len_arr(arr)

print(len_arr([1, 10, 10, 4, 5, 5, 2, 2, 43, 23]))


# Наибольшее число в списке
def max_arr(arr: list):
    if len(arr) == 1:
        return arr[0]
    else:
        if arr[0] > arr[1]:
            arr.pop(1)
            return max_arr(arr)
        else:
            arr.pop(0)
            return max_arr(arr)

print(max_arr([1, 10, 10, 4, 5, 55556, 2, 2, 43, 23]))

