n = int(input())
titles = [input() for _ in range(n)]
with open('output.txt', 'w', encoding='utf-8') as outfile:
    for title in titles:
        with open(f'{title}', encoding='utf8') as file:
            data = file.readlines()
            outfile.writelines(data)



