m = int(input())
surname_lists = []
for i in range(m):
    surname_list = set()
    for j in range(int(input())):
        surname_list.add(input())
    surname_lists.append(surname_list)
attendance = surname_lists[0]
for surnames in surname_lists:
    attendance = attendance.intersection(surnames)
print(*attendance)
