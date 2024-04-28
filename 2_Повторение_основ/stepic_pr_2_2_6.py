n = int(input())
mylist = []
for _ in range(n):
    mylist.append(int(input()))
z = int(input())

Flag = False
for i in mylist:
    y = mylist.copy()
    y.remove(i)
    for j in y:
        if i * j == z:
            Flag = True
            break
if Flag:
    print('ДА')
else:
    print('НЕТ')


