first_line, second_line = [set(input().split()) for _ in range(2)]
numbers = first_line & second_line
print(*sorted(numbers, key=int))