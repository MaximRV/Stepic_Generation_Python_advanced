n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
matrix_numbers = []
sum_row = round(n * ((n ** 2 + 1) / 2))

for k in range(0, n):
    if sum(matrix[k]) != sum_row or sum([row[k] for row in matrix]) != sum_row:
        print('NO')
        break
    else:
        sum_1 = 0
        sum_2 = 0
        for l in range(n - 1, -1, -1):
            sum_1 += matrix[l][l]
            sum_2 += matrix[n - 1 - l][l]
        if sum_1 != sum_2:
            print('NO')
            break
        else:
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] not in matrix_numbers:
                        matrix_numbers.append(matrix[i][j])
            if sum(matrix_numbers) == (n ** 2 * (n ** 2 + 1)) / 2:
                print('YES')
                break
            else:
                print('NO')
                break