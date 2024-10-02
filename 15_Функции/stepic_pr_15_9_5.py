a, b = [int(input()) for _ in range(2)]

print(*[x for x in range(a, b+1)  if "0" not in str(x) and all([x % int(i) == 0 for i in list(str(x))])])