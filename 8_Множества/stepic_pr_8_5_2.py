n = int(input())
line = ''
for _ in range(n):
    line += input().lower()
print(len(set(line)))
