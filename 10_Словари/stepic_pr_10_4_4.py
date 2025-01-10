dict_1 = {}
for _ in range(int(input())):
    key, value = input().split()
    dict_1[key] = value
    dict_1[value] = key

word = input()
print(dict_1[word])
