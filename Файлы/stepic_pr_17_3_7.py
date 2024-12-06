import random

with open('C:\\Users\\Максим\\first_names.txt', encoding='utf-8') as first_file, open(
    'C:\\Users\\Максим\\last_names.txt', encoding='utf-8') as second_file:
    first_names = first_file.read().splitlines()
    last_names = second_file.read().splitlines()

    for _ in range(3):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        print(f"{first_name} {last_name}")



