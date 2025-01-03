import re

result = {}
delimiters = r"[ .,!?:;-]"
rows_elements = re.split(delimiters, input())
words = [elem for elem in rows_elements if elem]

for word in words:
    word = word.lower()
    result[word] = result.get(word, 0) + 1

min_value = min(result.values())

key_m = ''
for key in result:
    if result[key] == min_value:
        if not key_m:
            key_m = key
        elif key < key_m:
            key_m = key

print(key_m)
