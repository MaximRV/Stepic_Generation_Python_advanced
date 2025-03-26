from fractions import Fraction as F
first_number = input()
second_number = input()
print(f'{first_number} + {second_number} = {F(first_number) + F(second_number)}')
print(f'{first_number} - {second_number} = {F(first_number) - F(second_number)}')
print(f'{first_number} * {second_number} = {F(first_number) * F(second_number)}')
print(f'{first_number} / {second_number} = {F(first_number) / F(second_number)}')