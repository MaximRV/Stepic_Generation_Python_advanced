rules_access_dict = {}
for _ in range(int(input())):
    elem_list = input().split()
    rules_access_dict[elem_list[0]] = elem_list[1:]

check_list = []
for _ in range(int(input())):
    check_list.append(input().split())

for elem in check_list:
    if elem[0] == 'execute':
        print('OK' if 'X' in rules_access_dict[elem[1]] else 'Access denied')
    else:
        print('OK' if elem[0][0].upper() in rules_access_dict[elem[1]] else 'Access denied')



