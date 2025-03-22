from decimal import *

number = Decimal(input())
expression = number.exp() + number.ln() + number.log10() + number.sqrt()
print(expression)