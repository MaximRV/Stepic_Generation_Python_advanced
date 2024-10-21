n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

if n <= m:
    cycle = n * 2 - 1
elif n > m != 1:
    cycle = m * 2
else:
    cycle = m * 2 - 1

n1 = 0
m1 = 0
matrix[n1][m1] = 1
for _ in range(cycle):
    while 0 <= m1 + 1 <= m - 1 and matrix[n1][m1 + 1] == 0:
        matrix[n1][m1 + 1] = matrix[n1][m1] + 1
        m1 += 1
    while 0 <= n1 + 1 <= n - 1 and matrix[n1 + 1][m1] == 0:
        matrix[n1 + 1][m1] = matrix[n1][m1] + 1
        n1 += 1
    while 0 <= m1 - 1 <= m - 1 and matrix[n1][m1 - 1] == 0:
        matrix[n1][m1 - 1] = matrix[n1][m1] + 1
        m1 -= 1
    while 0 <= n1 - 1 <= n - 1 and matrix[n1 - 1][m1] == 0:
        matrix[n1 - 1][m1] = matrix[n1][m1] + 1
        n1 -= 1

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end=' ')
    print()