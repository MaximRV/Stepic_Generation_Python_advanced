vocabular_1 = {}
for i in ''.join([v.strip('.,!?:;-') for v in input().split()]):
    vocabular_1[i.lower()] = vocabular_1.get(i, 0) + 1

vocabular_2 = {}
for i in ''.join([v.strip('.,!?:;-') for v in input().split()]):
    vocabular_2[i.lower()] = vocabular_2.get(i, 0) + 1

print('YES') if vocabular_1 == vocabular_2 else print('NO')