li = input().split()
result = [[]]
for i in range(len(li)):
    for j in range(len(li)):
        result.append(li[: j + 1])
    del li[0]

result = sorted(result, key=len)
print(result)
