import sys

input = sys.stdin.readline

num = int(input())
cnt = 9

for n in range(10, num + 1):
    str_n = str(n)
    for i in range(len(str_n) - 2):
        if int(str_n[i]) - int(str_n[i + 1]) != int(str_n[i + 1]) - int(str_n[i + 2]):
            cnt -= 1
            break
    cnt += 1

if num < 10:
    cnt = num

print(cnt)