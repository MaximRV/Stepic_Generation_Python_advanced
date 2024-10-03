password = input()

first_condition = len(password) >= 7
second_condition = any(map(lambda x: x.isdigit(), password))
third_condition = any(map(lambda x: x.isupper(), password))
fourth_condition = any(map(lambda x: x.islower(), password))

if all((first_condition, second_condition,third_condition,fourth_condition)):
    print("YES")
else:
    print("NO")

