dict_1 = {}
for _ in range(int(input())):
    number, name = input().split()
    dict_1[name.lower()] = dict_1.get(name.lower(), ()) + (number,)

for _ in range(int(input())):
    name = input().lower()
    if name in dict_1:
        print(*dict_1[name])
    else:
        print("абонент не найден")
