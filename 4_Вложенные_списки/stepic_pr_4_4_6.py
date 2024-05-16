n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

max_elem = matrix[0][0]

for i in range(n):
    for j in range(n):
        if (i >= j and i <= n - 1 -j) or (i <= j and  i >= n - 1 - j):
            if matrix[i][j] > max_elem:
                max_elem = matrix[i][j]

print(max_elem)