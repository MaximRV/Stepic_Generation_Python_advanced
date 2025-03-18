file_name = input()
with open(file_name, 'r', encoding='utf-8') as file:
    cursors_list = [0]
    nextСursor = file.readline()
    while nextСursor:
        cursors_list.append(file.tell())
        nextСursor = file.readline()
    file.seek(0)
    if len(cursors_list) <= 10:
        print(*file.readlines())
    else:
        file.seek(cursors_list[-11])
        print(file.read())