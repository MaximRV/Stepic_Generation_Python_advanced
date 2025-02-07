import random

length = int(input())    # длина пароля
number_list = [x for x in (list(range(65,91)) + list(range(97,123)))]
for _ in range(length):
    index = random.randint(0, len(number_list) -1 )
    print(chr(number_list[index]), end='')