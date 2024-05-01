my_str = input()
l = my_str.split('О')
total = 0
for i in l:
    if i.count('Р') > total:
        total = i.count('Р')
print(total)


