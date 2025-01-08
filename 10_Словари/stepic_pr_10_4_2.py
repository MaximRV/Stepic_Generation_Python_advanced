vocabular_1 = {}
for i in input():
    vocabular_1[i] = vocabular_1.get(i, 0) + 1

vocabular_2 = {}
for i in input():
    vocabular_2[i] = vocabular_2.get(i, 0) + 1

print('YES' if vocabular_1 == vocabular_2 else 'NO')