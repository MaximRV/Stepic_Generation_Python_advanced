n, m = [int(i) for i in (input().split())]
matrix = [[None] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = j * n + 1 + i


for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(3), end=' ')
        print()
