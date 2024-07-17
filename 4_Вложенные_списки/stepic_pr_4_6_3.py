n, m = [int(i) for i in (input().split())]
matrix = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0:
            matrix[i][j] = j + 1
        else:
            matrix[i][j] = matrix[i - 1][j] + m

for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(3), end=' ')
        print()
