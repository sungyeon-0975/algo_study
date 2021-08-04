a = input()
a_origin = a
cnt = 0

while True:
    a = a[-1] + str(int(a[0]) + int(a[1]))[-1]
    cnt += 1
    if a == a_origin:
        break

print(cnt)