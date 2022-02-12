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


arr = [0, 3, 43, 35, 3, 10, -10, 12, 4]
print(find_smallest(arr))
newarr = selection_sort(arr)
print(newarr)
