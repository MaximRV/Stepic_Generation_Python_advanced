from functools import reduce

print(*sorted(
    [input() for _ in range(int(input()))],
    key=lambda word: (
        reduce(lambda s, letter: s + ord(letter.upper()) - ord('A'), word, 0), word
    )
), sep='\n')



