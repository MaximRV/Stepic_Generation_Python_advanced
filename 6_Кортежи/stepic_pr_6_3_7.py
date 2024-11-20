n = int(input())
numbers = ()

for i in range(1, n + 1):
    if 1 <= i <= 3:
        numbers = numbers + (1,)
    else:
        numbers = numbers + (sum(numbers[i-4:i - 1]),)

print(*numbers)