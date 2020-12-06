n, m = map(int, input().split())
a_set = set()
b_set = set()
for i in range(n):
    a_set.add(int(input()))
for i in range(m):
    b_set.add(int(input()))

print(len(a_set.intersection(b_set)))
print(*sorted(a_set.intersection(b_set)))
print(len(a_set - b_set))
print(*sorted(a_set - b_set))
print(len(b_set - a_set))
print(*sorted(b_set - a_set))
