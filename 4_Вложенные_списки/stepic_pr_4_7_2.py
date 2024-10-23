n, m1 = [int(i) for i in input().split()]
matrix_a =[[int(i) for i in input().split()] for _ in range(n)]
input()
m2, k = [int(i) for i in input().split()]
matrix_b=[[int(i) for i in input().split()] for _ in range(m2)]

matrix_new = [[0] * k for _ in range(n)]

for i in range(n):
    for e in range(k):
        for j in range(m1):
            matrix_new[i][e] += matrix_a[i][j] * matrix_b[j][e]

for i in matrix_new:
    print(*i)

