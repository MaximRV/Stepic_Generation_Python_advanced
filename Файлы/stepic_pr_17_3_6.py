with open('C:\\Users\\Максим\\file.txt', encoding='utf-8') as file:
    line = file.read()
    total_letters = sum(c.isalpha() for c in line.replace("\n", ""))
    total_words = len(line.split())
    total_rows = len(line.split("\n"))
    print("Input file contains:")
    print(f"{total_letters} letters")
    print(f"{total_words} words")
    print(f"{total_rows} lines")
