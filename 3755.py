n = int(input())
num_all = set(range(1, n + 1))
nums = num_all
while True:
    answer = input()
    if answer == 'HELP':
        break

    answer = set(int(x) for x in answer.split())
    answer_2 = input()
    if answer_2 == 'YES':
        nums = nums.intersection(answer)
    else:
        nums = nums.intersection(num_all - answer)
print(*sorted(nums))
