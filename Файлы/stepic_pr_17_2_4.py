file = open("numbers.txt", 'r', encoding='utf-8')
print(sum([int(i) for i in file.readlines()]))
file.close()
