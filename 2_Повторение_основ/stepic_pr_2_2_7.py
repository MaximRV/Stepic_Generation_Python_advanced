answer_1 = input()
answer_2 = input()

if answer_1 == answer_2:
    print('ничья')

elif answer_1 == 'камень':
    if answer_2 == 'ножницы':
        print('Тимур')
    elif answer_2 == 'бумага':
        print('Руслан')

elif answer_1 == 'ножницы':
    if answer_2 == 'бумага':
        print('Тимур')
    elif answer_2 == 'камень':
        print('Руслан')

elif answer_1 == 'бумага':
    if answer_2 == 'ножницы':
        print('Руслан')
    elif answer_2 == 'камень':
        print('Тимур')