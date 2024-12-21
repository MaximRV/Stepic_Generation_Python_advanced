with open('goats.txt', encoding='utf8') as file, open(
        'answer.txt', 'w', encoding='utf-8') as outfile:
    colours = []
    while True:
        row = file.readline().splitlines()
        if row[0] == "GOATS":
            break
        colours.append(row)
    rows = file.read().splitlines()
    result = []
    for i in range(1, len(colours)):
        count = rows.count(colours[i][0])
        percentage = round((count / len(rows)) * 100)
        if percentage > 7:
           result.append(colours[i][0])
    for row in sorted(result):
        print(row, file=outfile)

