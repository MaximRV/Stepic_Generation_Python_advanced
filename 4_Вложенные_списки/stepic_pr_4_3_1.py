n = int(input())
li = []
for i in range(1, n + 1):
   li.append([i for i in range(1, n + 1)])
print(*li, sep='\n')
