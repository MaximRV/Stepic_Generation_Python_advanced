n= int(input())
matrix = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if (i >= j and i + j + 1 >= n) or (i <= j and i + j + 1 <= n):
            matrix[i][j] = 1


for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(3), end=' ')
        print()
