n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

total_1 = 0
total_2 = 0
total_3 = 0
total_4 = 0

for i in range(n):
    for j in range(n):
        if (i < j and i < n - 1 -j) :
            total_1 += matrix[i][j]
        elif (i < j and i > n - 1 -j) :
            total_2 += matrix[i][j]
        elif (i > j and i > n - 1 - j):
            total_3 += matrix[i][j]
        elif (i > j and i < n - 1 - j):
            total_4 += matrix[i][j]


print('Верхняя четверть:', total_1)
print('Правая четверть:', total_2)
print('Нижняя четверть:', total_3)
print('Левая четверть:', total_4)




