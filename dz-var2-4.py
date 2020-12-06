films = {}
n = int(input())
for i in range(n):
    film_string = input().split()
    films[film_string[0]] = {'жанр': film_string[1], 'страна': film_string[2], 'режисер': film_string[3],
                             'бюджет': film_string[4]}

counrtry = input()
flag = False
for film in films:
    if films[film]['страна'] == counrtry:
        print(film)
        flag = True

if not flag:
    print('''I don't know''')

4
мстители фантастика сша уидон 220000000
пятыйэлемент фантастика сша бессон 200000000
елки комедия европпа  бекмамбетов 300000000
гонка драма европпа ховард 200000000
сша
