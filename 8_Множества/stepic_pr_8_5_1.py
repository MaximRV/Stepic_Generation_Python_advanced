n = int(input())
words = [len(set(input().lower())) for _ in range(n)]
for word in words:
    print(word)