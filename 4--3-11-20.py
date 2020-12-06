print('Введите через пробел название страны, столицу, часть света, численность населения(млн чел.), '
      'площадь территории(тыс. кв. км)')
print('Например: Россия Москва Евразия 150 17100')

countries = {}

n = int(input('Ведите кол-во стран: '))
for i in range(n):
    c = input().split()
    countries[c[0]] = {'Столица': c[1], 'Часть света': c[2], 'Численность населения': c[3], 'Площадь': c[4]}

asia = []
ea = []
eu = []
for c in countries:
    if countries[c]['Часть света'] == 'Азия':
        asia.append(c)
    elif countries[c]['Часть света'] == 'Евразия':
        ea.append(c)
    else:
        eu.append(c)

print('Asia: ', *asia)
print('Eurasia: ', *ea)
print('Europe: ', *eu)