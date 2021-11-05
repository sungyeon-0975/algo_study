"""
python
    Memory - 40 MB
    Time - 0.184 s
"""
import sys
sys.stdin = open('input.txt')


N, S = map(int, sys.stdin.readline().split())
li = [0] + list(map(int, sys.stdin.readline().split()))

for i in range(1, len(li)):
    li[i] = li[i-1] + li[i]
         
l, r = 0, 1
answer = 1e10

while r < len(li):
    if li[r] - li[l] >= S:
        answer = min(answer, r-l)
        l += 1
    else:
        r += 1

if answer == 1e10:
    print(0)
else:
    print(answer)