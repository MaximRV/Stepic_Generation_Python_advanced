line = map(int,input().split())
numbers = set()
for elem in line:
    if elem in numbers:
        print("YES")
    else:
        print("NO")
        numbers.add(elem)
