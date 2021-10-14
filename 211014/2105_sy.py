import sys
sys.stdin = open('input.txt')


def find_sets(x, y):
    global res
    for a in range(y, 0, -1):
        for b in range(min(n-1-x-a, n-y-1), 0, -1):
            s = tour_rhombus(x, y, [b, a])
            if s:
                if len(s) > res:
                    res = len(s)


def tour_rhombus(x, y, ab):
    s = set()
    for i in range(4):
        for _ in range(ab[i % 2]):
            x += dx[i]
            y += dy[i]
            if l[x][y] in s:
                return {}
            s.add(l[x][y])
    return s


t = int(input())
dx = [1, 1, -1, -1]#우하,좌하,좌상,우상
dy = [1, -1, -1, 1]
for idx in range(1, t+1):
    n = int(input())
    l = [list(map(int, input().split())) for _ in range(n)]
    res = -1
    for i in range(n-2):
        for j in range(1, n-1):
            find_sets(i, j)

    print('#{} {}'.format(idx, res))
