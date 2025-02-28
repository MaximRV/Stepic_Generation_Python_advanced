with open(input(), 'r', encoding='utf-8') as file:
    count = 0
    for row in file:
        count += 1
    print(count)