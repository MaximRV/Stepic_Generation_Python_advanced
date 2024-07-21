
n, m = [int(i) for i in input().split()]
matrix = [list(range(1, m + 1))  for i in range(n)]

for i in range(1, len(matrix)):
    matrix[i] = matrix[i-1][1:] + matrix[i-1][:1]

for row in matrix:
    print(*row)
