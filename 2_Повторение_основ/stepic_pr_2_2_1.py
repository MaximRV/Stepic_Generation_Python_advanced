n = int(input())
li = []

count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0

for i in range(n):
    li.append(list(map(int,input().split())))

for i in li:
    if i[0] > 0 and i[1] > 0:
        count_1 += 1
    elif i[0] < 0 and i[1] > 0:
        count_2 += 1
    elif i[0] < 0 and i[1] < 0:
        count_3 += 1
    elif i[0] > 0 and i[1] < 0:
        count_4 += 1

print('Первая четверть:',count_1)
print('Вторая четверть:',count_2)
print('Третья четверть:',count_3)
print('Четвертая четверть:',count_4)
