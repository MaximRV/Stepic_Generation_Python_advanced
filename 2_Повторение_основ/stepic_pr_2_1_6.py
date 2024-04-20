st = input()
a = st[-5::]
print(int(st[:-5] + a[::-1]))
