from fractions import Fraction as F
from math import factorial

n = int(input())
total = 0
for i in range(1, n + 1):
    total += F(1,factorial(i))
print(total)