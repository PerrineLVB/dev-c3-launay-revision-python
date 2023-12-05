import random

my_list = [random.randint(1, 1000) for i in range(10)]
#print(my_list)

if len(my_list) == 0:
    print("Liste vide")
else:
    for i in my_list:
        print (i * i)