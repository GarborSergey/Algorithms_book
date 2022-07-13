# Поиск наименьшего числа в списке
def find_smallest(arr: list):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


# Сортировка массива выбором
def selection_sort(arr: list):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


x = [0, 3, 43, 35, 3, 10, -10, 12, 4]
print(find_smallest(x))
newarr = selection_sort(x)
print(newarr)


# Сортировка массива вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


array = [4, 22, 41, 40, 27, 31, 36, 1, 42, 39, 14, 9, 3, 6, 34, 9, 21, 4, 29, 49]
insertion_sort(array)
print("sorted: " + str(array))




