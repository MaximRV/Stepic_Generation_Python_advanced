octets_list = list(input().split("."))
res = all(map(lambda x: False if not x.isdigit() or int(x) > 255 else int(x[-3:]) in list(range(256)), octets_list))
print(res)