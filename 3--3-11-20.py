print('Введите через пробел название страны, столицу, часть света, численность населения(млн чел.), '
      'площадь территории(тыс. кв. км)')
print('Например: Россия Москва Евразия 150 17100')


countries = {}

n = int(input('Ведите кол-во стран: '))
for i in range(n):
    c = input().split()
    countries[c[0]] = {'Столица': c[1], 'Часть света': c[2], 'Численность населения': c[3], 'Площадь': c[4]}

c = input()
if c in countries:
    print(countries[c])
else:
    print('''I don't know''')