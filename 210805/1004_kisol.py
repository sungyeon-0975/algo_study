import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    T2 = int(input())
    cnt = 0
    
    for _ in range(T2):
        cx, cy, r = map(int, input().split())
        d1 = ((cx - x1) ** 2 + (cy - y1) ** 2) ** 0.5
        d2 = ((cx - x2) ** 2 + (cy - y2) ** 2) ** 0.5
        if (d1 < r and d2 > r) or (d1 > r and d2 < r):
            cnt += 1
    
    print(cnt)

