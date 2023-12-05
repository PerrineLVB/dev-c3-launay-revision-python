import random

my_list = [random.randint(1, 1000) for i in range(10)]
print('Random list', my_list)

if len(my_list) == 0:
    print("Empty list")
else:
    for i in range(1, len(my_list)):
        while i > 0 and my_list[i] < my_list[i-1]:
            my_list[i], my_list[i-1] = my_list[i-1], my_list[i]
            i -= 1
    print('Ordered list', my_list)