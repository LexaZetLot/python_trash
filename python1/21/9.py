from math import sqrt


def f1(arr):
    for i in range(len(arr)):
        arr[i] = sqrt(arr[i])

def f2(arr):
    return list(map((lambda x: sqrt(x)), arr))

def f3(arr):
    return [sqrt(x) for x in arr]

def f4(arr):
    return (sqrt(x) for x in arr)


list_arr = [2, 4, 9, 16, 25]
f1(list_arr)
print(list_arr)

list_arr = [2, 4, 9, 16, 25]
list_arr = f2(list_arr)
print(list_arr)

list_arr = [2, 4, 9, 16, 25]
list_arr = f3(list_arr)
print(list_arr)

list_arr = [2, 4, 9, 16, 25]
list_arr = f4(list_arr)
print(list(list_arr))