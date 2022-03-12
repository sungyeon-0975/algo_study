N, M = map(int, input().split())
mp = []

for _ in range(N):
    mp.append(list(map(int, list(input()))))

n = min(N, M)
brk = False

while n > 1:
    for i in range(N+1-n):
        for j in range(M+1-n):
            if mp[i][j] == mp[i+n-1][j+n-1] == mp[i+n-1][j] == mp[i][j+n-1]:
                brk = True
        if brk:
            break
    if brk:
        break

    n -= 1

print(n**2)
