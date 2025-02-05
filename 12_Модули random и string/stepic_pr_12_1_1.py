import random

n = int(input())
for _ in range(n):
    number = random.randrange(0,7)
    print('Орел' if number % 2 == 0 else "Решка")
