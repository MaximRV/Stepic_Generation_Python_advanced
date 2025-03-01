with open('ledger.txt', 'r', encoding='utf-8') as file:
    total = 0
    for row in file:
        total += int(row[1:])
    print(f'${total}')