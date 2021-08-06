import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for i in range(n):
        cx, cy, r = map(int, input().split())
        start = (((x1-cx)**2) + ((y1-cy)**2))**0.5
        end = (((x2-cx)**2) + ((y2-cy)**2))**0.5
        if (start < r and end > r) or (start > r and end < r):
            cnt += 1
    print(cnt)