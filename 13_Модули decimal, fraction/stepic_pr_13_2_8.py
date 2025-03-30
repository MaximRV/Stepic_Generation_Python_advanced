from math import gcd

fractions = []
n = int(input())

# Перебираем все возможные знаменатели
for denominator in range(2, n + 1):
     # Перебираем все возможные числители
    for numerator in range(1, denominator):
        # Проверяем, является ли дробь несократимой
        if gcd(numerator, denominator) == 1:
            fractions.append(f"{numerator}/{denominator}")

# Сортируем дроби по возрастанию
fractions.sort(key=lambda frac: eval(frac))  # eval используется для вычисления дроби как числа

    # Выводим дроби
for fraction in fractions:
    print(fraction)