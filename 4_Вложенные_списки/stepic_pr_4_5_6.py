n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]

for i in range(n // 2):
    for j in range(n):
        matrix[i][j], matrix[(i+1) * -1][j] = matrix[(i+1) * -1][j], matrix[i][j]

for row in matrix:
    print(*row)
