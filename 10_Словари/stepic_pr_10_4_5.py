n = int(input())
dict_1 = {}

for i in range(n):
    city = input().split()
    for i in city[1:]:
        dict_1[i] = city[0]

for _ in range(int(input())):
    city = input()
    print(dict_1[city])


