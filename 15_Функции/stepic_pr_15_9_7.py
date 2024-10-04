class_contains_five = []

for _ in range(int(input())):
    each_class_marks = []
    for _ in range(int(input())):
        each_class_marks.append(int(input()[-1]))
    class_contains_five.append(any(map(lambda x: x == 5, each_class_marks)))

print("YES" if all(class_contains_five) else "NO")

