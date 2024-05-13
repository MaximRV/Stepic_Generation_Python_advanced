n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))

total = 0
for i in range(n):
    total += matrix[i][i]

print(total)
