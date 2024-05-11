rows, cols = int(input()),int(input())
matrix = []
for _ in range(rows):
    temp = []
    for _ in range(cols):
        temp.append(input())
    matrix.append(temp)

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=' ')
    print()
