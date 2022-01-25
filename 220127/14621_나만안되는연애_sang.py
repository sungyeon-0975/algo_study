def union(a, b):
    a = find(a)
    b = find(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a


def find(a):
    if a == parent[a]:
        return a

    parent[a] = find(parent[a])
    return parent[a]


N, M = map(int, input().split())
lst = [0]+list(input().split())

edges = []
for _ in range(M):
    edges.append(tuple(map(int, input().split())))

edges.sort(key=lambda x: x[2])
parent = list(range(N+1))
ans, cnt = 0, 0

for u, v, d in edges:
    if find(u) != find(v) and lst[u] != lst[v]:
        union(u, v)
        ans += d
        cnt += 1

print(ans if cnt == N-1 else -1)
