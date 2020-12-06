films = {}
n = int(input())
for i in range(n):
    film_string = input().split()
    films[film_string[0]] = {'жанр': film_string[1], 'страна': film_string[2], 'режисер': film_string[3],
                             'бюджет': film_string[4]}

mean_b = 0
for film in films:
    mean_b += int(films[film]['бюджет'])
print(mean_b / n)

4
мстители фантастика сша уидон 220000000
пятыйэлемент фантастика сша бессон 200000000
елки комедия россия  бекмамбетов 300000000
гонка драма германия ховард 200000000