sum_num = 0
lists = []
for i in range(0, 255):
    lists.append((chr(i), i))
    sum_num += i
print(lists)
print(sum_num)
