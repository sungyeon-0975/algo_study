import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# 성별 S 여학생 0 남학생 1
# 학년 Y (1~6)

arr = [[0] * 2 for _ in range(6)] # row = 학년/col = 성별

for _ in range(N):
    s, y = map(int, input().split())
    arr[y-1][s] += 1

# print(arr)
rooms = 0
for i in range(6):
    for j in range(2):
        if arr[i][j] % K:
            rooms += (arr[i][j] // K) + 1
        else:
            rooms += arr[i][j] // K

print(rooms) # 제출 성공 (100점!)