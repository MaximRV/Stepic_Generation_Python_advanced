words_list = input().split()
words_dict = {}
for word in words_list:
    words_dict[word] = words_dict.get(word,0) + 1
    print(words_dict[word], end=' ')
