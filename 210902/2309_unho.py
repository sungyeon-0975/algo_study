import sys



num_list = [int(sys.stdin.readline()) for _ in range(9)]

num_list.sort()
reamin = sum(num_list) - 100
sign = False

for i in range(8):
    tmp_answer = num_list[i]
    for j in range(i+1, 9):
        tmp_answer += num_list[j]
        if tmp_answer == reamin:
            sign = True
            break
    if sign:
        break

num_list.pop(j)
num_list.pop(i)

for i in range(7):
    print(num_list[i])