from fractions import Fraction as F

n = int(input())
total = 0
for i in range(1, n + 1):
    total += F(1,i**2)
print(total)