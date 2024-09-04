numbers = list(map(int, input().split()))


def sort_key(x):
    return sum([int(i) for i in str(x)])


print(*sorted(numbers, key=sort_key))
