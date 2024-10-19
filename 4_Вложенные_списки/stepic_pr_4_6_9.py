n, m = [int(i) for i in input().split()]

matrix = [[0] * m for _ in range(n)]

num = 1
for i in range(n + m - 1):
    for j in reversed(range(max(0, i - n + 1), min(i + 1, m))):
        matrix[i - j][j] = num
        num += 1

for row in matrix:
    print(*row)
