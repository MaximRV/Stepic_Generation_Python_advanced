import random

surnames_list = [input() for _ in range(int(input()))]
available_friend = surnames_list.copy()
result = []

for elem in surnames_list:
    Flag = False
    if elem in available_friend:
        available_friend.remove(elem)
        Flag = True
    if len(available_friend) == 2 and Flag:
        if surnames_list[-1] == available_friend[0]:
            result.append(f'{elem} - {available_friend[0]}')
            available_friend.remove(available_friend[0])
        else:
            result.append(f'{elem} - {available_friend[1]}')
            available_friend.remove(available_friend[1])
        available_friend.append(elem)
    else:
        friend = random.choice(available_friend)
        if Flag:
            available_friend.append(elem)
        result.append(f'{elem} - {friend}')
        available_friend.remove(friend)
for row in result:
    print(row)
