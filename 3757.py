lang = [set(input() for j in range(int(input()))) for i in range(int(input()))]
all = set.intersection(*lang)
sb = set.union(*lang)
print(len(all))
print(*sorted(all), sep='\n')
print(len(sb))
print(*sorted(sb), sep='\n')