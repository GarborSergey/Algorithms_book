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


count_down1(5)


# Рекурсивная функция по вычислению факториала
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


print(fact(5))