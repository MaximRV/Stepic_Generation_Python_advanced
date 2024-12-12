with open('class_scores.txt', encoding='utf-8') as input_file, open(
        'new_scores.txt', 'w', encoding='utf-8') as outfile:
    rows = input_file.readlines()
    for row in rows:
        name, score = row.split()
        new_score = min(int(score) + 5, 100)
        print(f"{name} {new_score}", file=outfile)


