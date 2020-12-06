fin = open('input.txt')
classes = [[] for i in range(11)]
classes_new = []


def max2(array):
    m1 = array[-1]
    for i in range(len(array) - 1,-1, -1):
        if array[i] < m1:
            return array[i]
            break


for s in fin:
    c = s.split()
    classes[int(c[2]) - 1].append(int(c[3]))
for c in classes:
    if len(c) > 0:
        c = sorted(c)
        classes_new.append(max2(c))

for c in classes_new:
    print(c, end=' ')

