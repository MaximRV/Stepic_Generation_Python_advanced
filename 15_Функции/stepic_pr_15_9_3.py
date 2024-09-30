abscissas, ordinates, applicates=(map(float, input().split()) for _ in range(3))

radius = 2

res = [(x ** 2 + y ** 2 + z ** 2) <= radius ** 2 for x, y, z in zip(abscissas, ordinates, applicates)]

print(all(res))