import random

rand_list = [random.randint(1,20) for _ in range(0,20)]

list_comprehension_below_10 = [number for number in rand_list if number<10]

list_comprehension_below_10 = list(filter(lambda x: x<10 , rand_list))


print(rand_list, list_comprehension_below_10, list_comprehension_below_10)