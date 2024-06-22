d = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "}
n = input()

spisok = []

for item in d.items():
    spisok.append(item)

for elem in n.upper():
    for i in spisok:
        if elem in i[1]:
            ind = i[1].index(elem)
            print(i[0] * (ind + 1), end='')
