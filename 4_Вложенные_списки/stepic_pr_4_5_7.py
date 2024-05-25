n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
matrix_turn = [[matrix[j][i] for j in range(n - 1, -1, -1)] for i in range(n)]
for row in matrix_turn:
    print(*row)

