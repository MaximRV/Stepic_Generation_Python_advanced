def chunked(li, n):
    result = []
    for i in range(0,len(li),n):
        result.append(li[i:i + n])
    return result

li = input().split()
n = int(input())
print(chunked(li, n))
