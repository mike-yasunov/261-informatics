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
