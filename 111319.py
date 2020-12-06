from string import punctuation
string = input().lower().replace(' ', '')
letters = []
max_len = 0
max_len_letters = ''
for l in string:
    if l not in letters and l not in punctuation:
        letters.append(l)

for letter in letters:
    if string.count(letter) > max_len:
        max_len = string.count(letter)

for letter in letters:
    if string.count(letter) == max_len:
        max_len_letters += letter.upper()

print(max_len_letters)
print(max_len)
