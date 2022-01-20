import sys

t = int(input())
for _ in range(t):
    n = int(input())
    mp = []
    for _ in range(n+2):
        mp.append(list(map(int, sys.stdin.readline())))

    fw = [[0]*(n+2) for _ in range(n+2)]

    for i in range(n+2):
        for j in range(i+1, n+2):
            if abs(mp[i][0] - mp[j][0]) + abs(mp[i][1] - mp[j][1]) <= 1000:
                fw[i][j] = fw[j][i] = 1

    for k in range(n+2):
        for i in range(n+2):
            for j in range(i, n+2):
                if fw[i][j]:
                    continue

                if fw[i][k] and fw[k][j]:
                    fw[i][j] = fw[j][i] = 1

    print("happy" if fw[0][-1] else "sad")
