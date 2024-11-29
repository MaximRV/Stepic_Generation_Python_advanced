file = open('prices.txt','r',encoding='utf-8')
rows_list = [i.split('\t') for i in file.read().split('\n')]
file.close()
total = 0
for row in rows_list:
    if any(row):
        total += int(row[1]) * int(row[2])
print(total)
