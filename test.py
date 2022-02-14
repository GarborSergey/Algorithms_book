def sum_arr(arr: list):
    if len(arr) == 0:
        return 0
    else:
        x = arr[0]
        arr.pop(0)
        return x + sum_arr(arr)


x = [1, 10, 10]
print(sum_arr(x))
y = []

