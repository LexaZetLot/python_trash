arr = [1, 2, 3, 4]
arr[2] = []
print(arr)
arr[2:3] = []
print(arr)
del arr[0]
print(arr)
del arr[1:]
print(arr)