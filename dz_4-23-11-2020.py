ingredients_in_fridge = set()
ingredients = set()
recepts_is_avalible = []

m = int(input())
for i in range(m):
    ingredients_in_fridge.add(input())

n = int(input())
for i in range(n):
    recept_name = input()
    k = int(input())
    flag = True
    
    for j in range(k):
        ingredients.add(input())

    for i in ingredients:
        if not i in ingredients_in_fridge:
            flag = False

    if flag:
        recepts_is_avalible.append(recept_name)
    ingredients = set()

print(*recepts_is_avalible, sep='\n')
