with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt','w',encoding='utf-8') as output_file:
    rows = input_file.read().splitlines()
    for index, value in enumerate(rows, start=1):
        print(f'{index}) {value}', file=output_file)
