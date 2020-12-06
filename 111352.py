fin = open('input.txt')
fout = open('output.txt', 'w')
c = fin.readline()
school = [[0]*2 for i in range(100)]
while len(c) > 0:
    b = c.split()
    school[int(b[2])][0] += int(b[3])
    school[int(b[2])][1] += 1
    c = fin.readline()
schoolsrball = []
schools = []
for i in range(100):
    if school[i][1] > 0:
        schoolsrball.append(school[i][0])
        schools.append(i)
for i in range(len(schoolsrball)):
    for j in range(i):
        if schoolsrball[i] < schoolsrball[j]:
            schoolsrball[i], schoolsrball[j] = schoolsrball[j], schoolsrball[i]
            schools[i], schools[j] = schools[j], schools[i]
        elif schoolsrball[i] == schoolsrball[j] and schools[i] > schools[j]:
            schools[i], schools[j] = schools[j], schools[i]
for i in schools[::-1]:
    print(i, end=' ')
