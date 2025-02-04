result = {}
for _ in range(int(input())):
    items = input().split()
    value = int(items[2])
    if items[0] in result:
        result[items[0]][items[1]] = result[items[0]].get(items[1], 0) + value
    else:
        result[items[0]] = {items[1]: value}

for key in sorted(result):
    print(f'{key}:')
    for elem in sorted(result[key]):
        print(f'{elem} {result[key][elem]}')

