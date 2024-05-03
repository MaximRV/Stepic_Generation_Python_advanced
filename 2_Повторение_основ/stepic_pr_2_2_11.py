word = input() + ' запретил букву'
n = len(set(word.replace(' ', '')))
alf = [chr(i) for i in range(1072, 1104)]
for j in range(32):
    if alf[j] in word:
        word = " ".join(word.split())
        print(word + ' ' + alf[j])
        word = word.replace(alf[j], '')
