fin = open('input.txt')
m = int(input())
n = int(input())
knigi = set()
for i in range(m):
    c = fin.readline()
    knigi.add(c[:-1])

for i in range(n):
    if input() in knigi:
        print('YES')
    else:
        print('NO')