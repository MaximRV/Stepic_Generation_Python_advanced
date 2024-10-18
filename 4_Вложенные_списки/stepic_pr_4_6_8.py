n, m = [int(i) for i in input().split()]

matrix = [list(range(1, m + 1))  for i in range(n)]
for i in range(1,n):
    for j in range(m):
        if i % 2 != 0:
            matrix[i][-j - 1] = matrix[i - 1][j] + m
        else:
            matrix[i][j] = matrix[i - 1][0] + j + 1

for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(3), end=' ')
        print()

