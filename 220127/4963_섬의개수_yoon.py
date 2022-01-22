import sys
sys.stdin = open('4963_input.txt')
# input = sys.stdin.readline

while True:
    w, h = map(int, input().split())
    ans = 0
    if w == 0 and h == 0:
        break
    arr = [[0] * h for _ in range(w)]
    for i in range(w):
        for j in range(h):
            pass
