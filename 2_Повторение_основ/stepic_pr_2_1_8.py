n = int(input())
k = int(input())
li = [i for i in range(1, n + 1)]
while len(li) > 1:
    ind_del = k % len(li) - 1
    if len(li) == 2:
        li.pop(ind_del)
    else:
        if ind_del == -1:
            li = li[:ind_del]
        else:
            li = li[ind_del + 1:] + li[:ind_del]

print(*li)
