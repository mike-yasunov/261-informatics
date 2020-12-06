list1 = set()
list2 = set()

c = input()
while c.isdigit():
    list1.add(int(c))
    c = input()

c = input()
while c.isdigit():
    list2.add(int(c))
    c = input()

if len(list1.intersection(list2)) > 0:
    print(*sorted(list(list1.intersection(list2))), sep='\n')

else:
    print('EMPTY')

# 10
# 23
# 31
1

# 5
# 10
# 49
# 31
