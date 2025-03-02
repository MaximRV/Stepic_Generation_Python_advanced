with open('grades.txt', 'r', encoding='utf-8') as file:
    total = 0
    for row in file:
        mark_list = [int(i) for i in row.split(" ")[1:]]
        if min(mark_list) >= 65:
         total += 1
    print(total)