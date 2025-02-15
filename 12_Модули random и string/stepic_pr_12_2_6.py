import random

matrix = [ ["0"] * 5 for _ in range(5)]
numbers = random.sample(range(1,76), 25)
for i in range(5):
    for j in range(5):
        if i == 2 and j == 2:
            matrix[i][j] = 0
        else:
            matrix[i][j] = numbers[int(str(i) + str(j)) - i * 5]


for r in range(5):
        for c in range(5):
            print(str(matrix[r][c]).ljust(3), end=' ')
        print()