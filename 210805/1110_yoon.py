num = int(input())
res = num
temp = 0
count = 0

while True:
    temp = num//10 + num%10
    num = (num%10)*10 + temp%10
    count += 1
    if res == num:
        break

print(count)