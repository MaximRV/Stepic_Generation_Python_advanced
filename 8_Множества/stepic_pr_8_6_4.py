n = int(input())
numbers = set(int(i) for i in input())
for _ in range(n - 1):
    numbers = numbers & set(int(i) for i in input())
print(*sorted(numbers))