n, m = [int(i) for i in input().split()]
first_matrix = [[int(i) for i in input().split()] for _ in range(n)]
input()
seconed_matrix = [[int(i) for i in input().split()] for _ in range(n)]

new_matrix = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        new_matrix[i][j] = first_matrix[i][j] + seconed_matrix[i][j]

for row in new_matrix:
    print(*row)