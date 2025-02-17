import string
import random


def generate_password(length):
    elements = [i for i in string.printable[:62] if i not in "lI1oO0"]
    password = random.sample(elements, length)
    return ''.join(password)


def generate_passwords(count, length):
    passwords_list = []
    for _ in range(count):
        passwords_list.append(generate_password(length))
    return passwords_list


n, m = int(input()), int(input())
for elem in generate_passwords(n, m):
    print(elem)
