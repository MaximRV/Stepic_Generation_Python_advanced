letter_cost = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}
word_cost = 0
for letter in input():
    for key in letter_cost:
        if letter in letter_cost[key]:
            word_cost += key
print(word_cost)