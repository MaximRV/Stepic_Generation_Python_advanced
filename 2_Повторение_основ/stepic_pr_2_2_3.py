li = list(map(int,input().split()))
if len(li) % 2 == 0:
    for i in range(0,len(li),2):
        li[i],li[i+1] = li[i + 1],li[i]
else:
    for i in range(0,len(li)-1,2):
        li[i],li[i+1] = li[i + 1],li[i]

print(*li)
