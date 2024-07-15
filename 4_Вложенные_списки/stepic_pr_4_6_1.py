n,m = [int(i) for i in input().split()]
matrix = [['.'] * m for i in range(n)]
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            if j % 2 != 0:
                matrix[i][j] = "*"
    else:
        for j in range(len(matrix[i])):
            if j % 2 == 0:
                matrix[i][j] = "*"

for row in matrix:
    print(*row)
