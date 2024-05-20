n, m = int(input()), int(input())
matrix = [input().split() for _ in range(n)]
my_list = sorted(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if j == my_list[0]:
            matrix[i][j], matrix[i][my_list[1]] = matrix[i][my_list[1]], matrix[i][j]

for r in range(n):
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()
