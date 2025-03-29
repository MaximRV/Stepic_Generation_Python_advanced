from fractions import Fraction as F
from math import gcd
n = int(input())

numerator = n // 2
denominator = n - numerator

while gcd(numerator, denominator) != 1:
    numerator -= 1
    denominator += 1

print(F(numerator,denominator))