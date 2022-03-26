N, M = map(int, input().split())
ans = 0
s = set()
for _ in range(N):
    s.add(input())


for _ in range(M):
    w = input()
    if w in s:
        ans += 1

print(ans)
