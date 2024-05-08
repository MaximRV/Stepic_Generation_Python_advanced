my_str = input().split()
result = []
count = 0
for i in range(len(my_str)):
    if i == (len(my_str) - 1):
        result.append(my_str[i - count:i + 1])
        count = 0
    else:
        if my_str[i] == my_str[i + 1]:
            count += 1
            continue
        else:
            result.append(my_str[i - count:i + 1])
            count = 0

print(result)