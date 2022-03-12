from collections import defaultdict, deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
dct = defaultdict(list)

for _ in range(m):
    x, y = map(int, input().split())
    dct[x].append(y)
    dct[y].append(x)

v = [0]*(n+1)

dq = deque([a])

while dq:
    e = dq.popleft()

    for i in dct[e]:
        if not v[i]:
            v[i] = v[e] + 1
            dq.append(i)


print(v[b] if v[b] else -1)

