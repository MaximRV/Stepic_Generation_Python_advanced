n, m = int(input()),int(input())

matrix = [[input() for _ in range(m)] for _ in range(n)]

for row in matrix:
    print(*row)

print()

for i in range(m):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()

