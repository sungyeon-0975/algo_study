import sys
K,N = map(int,sys.stdin.readline().split())

cm_list = []
for i in range(K):
    cm = int(sys.stdin.readline())
    cm_list.append(cm)

low, high = 1, max(cm_list)

while low <= high:
    mid = (low+high)//2
    cnt = 0

    for cm in cm_list:
        cnt += cm//mid
    
    if cnt >= N:
        low = mid + 1
    else:
        high = mid -1

print(high)