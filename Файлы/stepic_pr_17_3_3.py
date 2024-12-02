with open('C:\\Users\\Максим\\lines.txt', encoding='utf-8') as file:
    row_list = list(map(str.strip, file.readlines()))
    max_len = max(map(len, row_list))
    for row in row_list:
        if len(row) == max_len:
            print(row)