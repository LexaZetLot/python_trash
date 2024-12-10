from _number import *

num = new_Number(1)
Number_add(num, 4)
Number_display(num)
Number_sub(num, 2)
Number_display(num)
print(Number_square(num))

Number_data_set(num, 99)
print(Number_data_get(num))
Number_display(num)
print(num)
delete_Number(num)