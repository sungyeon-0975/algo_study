import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')

'''
29200KB	72ms
'''

fruit = int(input())
dir, meter = [], []
box, sub = 1, 1

for _ in range(6):
    d, m = map(int, input().split())
    dir.append(d)
    meter.append(m)

for i in range(4):
    if dir.count(i+1) == 1:
        idx = dir.index(i+1)
        box *= meter[idx]
        sub *= meter[(idx+3) % 6]

print((box-sub)*fruit)