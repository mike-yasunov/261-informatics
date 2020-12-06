fin = open('input.txt')
word_set = set()
for s in fin:
    for w in s.split():
        word_set.add(w)
print(len(word_set))