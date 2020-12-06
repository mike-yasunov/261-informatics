fin = open('24-s1.txt')
c = 0
flag = False
for s in fin:
    for i in range(len(s)):
        if s[i] == 'Z' and s[i+2:i+4] == 'RO':
            flag = True
    if flag:
        c += 1
print(c)