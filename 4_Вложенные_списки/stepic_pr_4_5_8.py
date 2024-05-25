pozition = list(input())
n = 8
matrix = [['.'] * n for _ in range(n)]
knight = [(n - int(pozition[1])), (ord(pozition[0]) - 97)]
matrix[knight[0]][knight[1]] = 'N'
moves = [[1, 2], [2, 1], [-1, -2], [-2, -1], [-1, 2], [-2, 1], [1, -2], [2, -1]]

for i in moves:
    if 0 <= knight[1] + i[0] <= n - 1 and 0<= knight[0] + i[1] <= n - 1:
        matrix[knight[0] + i[1]][knight[1] + i[0]] = '*'

for row in matrix:
    print(*row)

