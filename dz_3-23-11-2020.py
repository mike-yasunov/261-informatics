workers = set()
workers_new = set()
n = int(input())
counter = 0
for i in range(n):
    surname = input()
    if surname in workers:
        counter += 1
        workers_new.add(surname)
    else:
        workers.add(surname)
print(counter + len(workers_new))
