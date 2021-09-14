import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')

'''
68500KB / 608ms
'''

N, H = map(int, input().split())
s = [0] * (H+1) # 석순
j = [0] * (H+1) # 종유석
cnt, section = N, 0

for i in range(N):
    if not i % 2:
        s[int(input())] += 1
    else:
        j[int(input())] += 1

for i in range(H-1, 0, -1): # 뒤에서부터 누적
    s[i] += s[i + 1]
    j[i] += j[i + 1]

for i in range(1, H+1):
    if cnt > (s[i] + j[H-i+1]):
        cnt = (s[i] + j[H-i+1])
        section = 1
    elif cnt == (s[i] + j[H-i+1]):
        section += 1

print(cnt, section)