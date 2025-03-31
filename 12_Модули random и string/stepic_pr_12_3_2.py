import random

n = 10**6       # количество испытаний

import random


inside_circle = 0

for _ in range(n):
    x = random.uniform(-1, 1)  # Генерируем случайное число x
    y = random.uniform(-1, 1)  # Генерируем случайное число y

        # Проверяем, попадает ли точка (x, y) внутрь круга
    if x**2 + y**2 <= 1:
        inside_circle += 1

    # Приближенное значение π
pi_approximation = (inside_circle / n) * 4
print(pi_approximation)