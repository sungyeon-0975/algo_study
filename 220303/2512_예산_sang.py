n = int(input())
lst = list(map(int, input().split()))
max_b = int(input())
s, e = 0, max(lst)
lst.sort()

while s <= e:
    m = (s+e)//2

    tmp = 0
    for i in range(n):
        if lst[i] < m:
            tmp += lst[i]
        else:
            break

    tmp += m * (n-i)

    if tmp > max_b:
        e = m - 1
    else:
        s = m + 1

print(e)
