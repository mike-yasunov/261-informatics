print('--------------1-------------')
print()

m = int(input())
cities = set()
for i in range(m):
    city = input()
    if city not in cities:
        cities.add(city)
city = input()
if city not in cities:
    print('OK')
else:
    print('TRY ANOTHER')

# 3
# Лондон
# Москва
# Нью-Йорк
# Париж
print()
print('--------------2-------------')
print()

m = int(input())
n = int(input())
eng = set()
nem = set()

for i in range(m):
    surname = input()
    eng.add(surname)

for i in range(n):
    surname = input()
    nem.add(surname)

counter = eng.intersection(nem)

if len(counter) > 0:
    print(len(counter))
else:
    print('NO')

# 3
# 2
# Иванов
# Петров
# Васечкин
# Иванов
# Михайлов


print()
print('--------------3-------------')
print()

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

# 5
# 10
# 49
# 31
