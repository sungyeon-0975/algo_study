a = int(input())
b = int(input())
c = int(input())
num = str(a * b * c)

for digit in range(10):
    cnt = 0
    for i in num:
        if i == str(digit):
            cnt += 1
    print(cnt)
