n = int(input())
result = []
word = 'anton'
for i in range(1, n+1):
    my_str = input()
    li = []
    for j in range(len(my_str)):
        if my_str[j] == 'n' and (len(li) == 1 or len(li) == 4):
            li.append(my_str[j])
        elif my_str[j] in word and word.find(my_str[j]) == len(li) and my_str[j] != 'n' :
            li.append(my_str[j])
    if ''.join(li) =='anton':
        result.append(i)

print(*result)