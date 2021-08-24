n = int(input())
l = [-1] + list(map(int, input().split()))


def boy(number):
    loc = number
    while loc <= n:
        l[loc] = 1-l[loc]
        loc += number


def girl(number):
    cnt = min(number - 1, n-number) + 1
    l[number] = 1 - l[number]
    for i in range(1, cnt):
        h, t = number-i, number+i
        if l[h] == l[t]:
            l[h] = 1 - l[h]
            l[t] = 1 - l[t]
        else:
            break


student_num = int(input())
for _ in range(student_num):
    gender, num = map(int, input().split())
    if gender == 1:
        boy(num)
    elif gender == 2:
        girl(num)

#출력
l.pop(0)
for i in range(n//20):
    for idx in range(i*20, (i+1)*20):
        print(l[idx], end=' ')
    print()
for idx in range(n - n%20, n):
    print(l[idx], end=' ')