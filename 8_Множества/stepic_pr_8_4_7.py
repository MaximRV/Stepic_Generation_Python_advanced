line = input().strip()+input().strip()
print(line)
if len(set(line)) == 10:
    print("YES")
else:
    print("NO")
