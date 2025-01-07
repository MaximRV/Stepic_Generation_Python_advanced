n = int(input())
vocabulary = {}
for _ in range(n):
    key, value = input().split(': ')
    vocabulary[key.lower()] = value
k = int(input())
for _ in range(k):
    word = input().lower()
    print(vocabulary[word]) if word in vocabulary else print("Не найдено")