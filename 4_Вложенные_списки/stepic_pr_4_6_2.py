n = int(input())

matrix = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i + j + 1 == n:
            matrix[i][j] = 1
        elif i + j + 1 < n:
            matrix[i][j] = 0
        elif i + j + 1 > n:
            matrix[i][j] = 2

for row in matrix:
    print(*row)
