n = int(input())
matrix = [input().split() for i in range(n)]
for i in range(n - 1):
    Flag = False
    if [matrix[i + j][i] for j in range(n - i)] == [matrix[i][i + j] for j in range(n - i)]:
        Flag = True
    else:
        print("NO")
        break

if Flag:
    print("YES")


