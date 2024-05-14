n = int(input())
matrix = []

for i in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

for i in range(n):
    count = 0
    sr_arefm = sum(matrix[i]) / n
    for j in range(n):
        if matrix[i][j] > sr_arefm:
            count += 1
    print(count)
