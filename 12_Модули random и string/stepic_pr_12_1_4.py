import random

numbers = [random.randint(0,49) for _ in  range(7)]
for number in sorted(numbers):
    print(number,end=' ')