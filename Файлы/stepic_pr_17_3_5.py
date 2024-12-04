with open('C:\\Users\\Максим\\nums.txt', encoding='utf-8') as file:
    line = file.read()
    numbers = ''.join(c if c.isdigit() else ' ' for c in line).split()
    total = sum(list(map(int,numbers)))
    print(total)
