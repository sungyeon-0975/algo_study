import sys
input = sys.stdin.readline

T, N = map(int, input().split())
cables = []

min_len = 0

for _ in range(T):
    cables.append(int(input()))

cnt = 0
cnt_cables = 0
left = 1
right = sum(cables) // N
min_len = 0

while True:
    center = (left + right) // 2
    print(left, center, right, cnt_cables)
    if min_len == center:
        break
    for idx in range(len(cables)):
        cnt += 1
        cnt_cables += cables[idx] // center
        # rest = len(cables) - idx - 1
        # if rest:
        #     possible_cables = cnt_cables + (sum(cables[idx + 1:]) // min_len)
        #     if possible_cables < N:
        #         break
    if cnt_cables < N:
        right = center - 1
    else:
        left = center + 1
    
    cnt_cables = 0
    min_len = center
    

print(min_len, cnt)


import sys
input = sys.stdin.readline

T, N = map(int, input().split())
cables = []

min_len = 0

for _ in range(T):
    cables.append(int(input()))

cnt_cables = 0
left = 1
right = sum(cables) // N
min_len = 0

while True:
    center = (left + right) // 2
    if min_len == center:
        break
    for idx in range(len(cables)):
        cnt_cables += cables[idx] // center
    if cnt_cables < N:
        right = center - 1
    else:
        left = center + 1
    cnt_cables = 0
    min_len = center

print(min_len)
