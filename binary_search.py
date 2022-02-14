# Бинарный поиск
def binary_search(list: list, item):
    # В этих переменных хранятся границы той части списка
    # в которой происходит поиск
    low = 0
    high = len(list) - 1
    i = 0

    while low <= high:  # Пока граница не сократиться до одного элемента
        i += 1
        print('attempt ', i)
        mid = int((low + high) / 2)  # Проверяем средний элемент
        guess = list[mid]
        if guess == item:  # Значение найдено
            return mid + 1
        if guess > item:  # Много
            high = mid - 1
        else:  # Мало
            low = mid + 1
    return None  # Значение не существует


my_list = range(120)

x = binary_search(my_list, 0)
print(x)
print(*my_list)
print(len(my_list))
