with open('C:\\Users\\Максим\\data.txt', encoding='utf-8') as file:
    row_list = list(map(str.strip, file.readlines()))
    print(*row_list[::-1], sep='\n')
