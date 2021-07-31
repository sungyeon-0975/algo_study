N = int(input())

def make_new(a):
    if a >= 10:
        new = int((a/10) + (a%10))
        return  int(str(a)[-1] + str(new)[-1])

    elif 0 <= a < 10:
        new = a
        return  int(str(a) + str(new))

new = 0
cnt = 1
restore = make_new(N)


while restore != N:
    cnt += 1
    restore = make_new(restore)


print(cnt)


