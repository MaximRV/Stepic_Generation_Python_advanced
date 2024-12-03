with open('C:\\Users\\Максим\\numbers.txt', encoding='utf-8') as file:
     for row in file:
        print(sum([int(row) for row in row.split()]))


