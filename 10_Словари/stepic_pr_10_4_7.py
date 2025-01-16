text = input()
dict_from_text, dict_letter = {}, {}
for i in text:
    dict_from_text[text.count(i)] = i
for i in range(int(input())):
    value, key = input().split(': ')
    new_key = dict_from_text[int(key)]
    dict_letter[new_key] = value
for i in text:
    print(dict_letter[i], end="")
