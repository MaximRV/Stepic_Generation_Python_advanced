import random


def generate_ip():
    numbers = [i for i in range(0, 256)]
    part_ip = random.sample(numbers, 4)
    return '.'.join([str(i) for i in part_ip])


print(generate_ip())
