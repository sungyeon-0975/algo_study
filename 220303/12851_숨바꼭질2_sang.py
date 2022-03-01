from collections import deque

N, K = map(int, input().split())

dq = deque([N])
v = [0]*1000001
ans = [100000, 0]


while dq:
    e = dq.popleft()
    if v[e] > ans[0]:
        break

    if e == K:
        ans[0] = v[e]
        ans[1] += 1
        continue

    for i in (e-1, e+1, e*2):
        if 0 <= i < 100001:
            if not v[i] or v[i] == v[e] + 1:
                v[i] = v[e] + 1
                dq.append(i)


print(*ans, sep="\n")
