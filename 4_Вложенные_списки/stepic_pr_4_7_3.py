n = int(input())
matrix_a =[[int(i) for i in input().split()] for _ in range(n)]
m = int(input())

matrix_b=[k[:] for k in matrix_a]
matrix_new = [[0] * n for _ in range(n)]

for _ in range(m - 1):
    for i in range(n):
        for e in range(n):
            for j in range(n):
                matrix_new[i][e] += matrix_a[i][j] * matrix_b[j][e]
    matrix_b = matrix_new
    matrix_new = [[0] * n for _ in range(n)]

for i in matrix_b:
    print(*i)

