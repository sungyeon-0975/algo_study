import sys
input = sys.stdin.readline

def solve(arr):
    total = 0
    temp_h = arr[0][1]
    temp_n = arr[0][0]
    for i in range(1, len(arr)):
        if arr[i][1] >= temp_h:
            total += temp_h * abs(arr[i][0]-temp_n)
            temp_h = arr[i][1]
            temp_n = arr[i][0]
    return total

N = int(input())
box = []
for n in range(N):
    L, H = map(int, input().split())
    box.append((L, H))
box.sort(key=lambda x:x[0])

pivot_idx = 0
for i in range(N):
    if box[i][1] > box[pivot_idx][1]:
        pivot_idx = i
left = box[0:pivot_idx+1]
right = list(reversed(box[pivot_idx:N]))

print(solve(left) + solve(right) + box[pivot_idx][1])