import sys
sys.stdin = open('4963_input.txt')
# input = sys.stdin.readline

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [[0] * h for _ in range(w)]