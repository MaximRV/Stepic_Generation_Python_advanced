with open('words.txt', 'r', encoding='utf-8') as file:
    words = file.readline().split(' ')
    max_len = max([len(el) for el in words])
    result = filter(lambda x: len(x) == max_len,words)
    print(*result, sep='\n')


