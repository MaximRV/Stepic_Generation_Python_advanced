li = input().split()
res = []
res.append(li[-1])
for i in range(len(li) - 1):
    res.append(li[i])
print(*res)