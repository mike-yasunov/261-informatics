num = list(input().split())
num_set = set()
for n in num:
    if n in num_set:
        print('YES')
    else:
        print('NO')
        num_set.add(n)
