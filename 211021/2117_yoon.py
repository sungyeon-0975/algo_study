import sys
sys.stdin = open('2117_input.txt')


def secure(i, j, k):
    temp = 0
    for r in range(N):
        for c in range(N):
            if abs(i-r) + abs(j-c) < k and arr[r][c]:
                temp += 1
    return temp


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    num = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                num += 1
    ans = 0

    for k in range(N+1, 0, -1):
        cost = k * k + (k-1) * (k-1)
        if cost > num * M:
            continue
        house = 0
        for i in range(N):
            for j in range(N):
                tmp = secure(i, j, k)
                if tmp > house:
                    house = tmp
        if house * M >= cost:
            ans = house
            break

    print('#{} {}'.format(t, ans))