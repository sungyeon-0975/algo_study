import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp_R = [-1] * N             # 현재 위치에서 빨간색 선택한 경우 최솟값
dp_G = [-1] * N             # 초록색 선택한 경우 최솟값
dp_B = [-1] * N             # 파란색 선택한 경우 최솟값

dp_R[0] = li[0][0]          # 첫번째 값 추가
dp_G[0] = li[0][1]
dp_B[0] = li[0][2]

for i in range(1, N):
    dp_R[i] = min(dp_G[i-1] + li[i][0], dp_B[i-1] + li[i][0])   # 이전에 다른 색을 골라야하므로
    dp_G[i] = min(dp_R[i-1] + li[i][1], dp_B[i-1] + li[i][1])   # ex) 현재 빨간색 선택시 이전에 초록 파랑 선택한 최솟값에서
    dp_B[i] = min(dp_R[i-1] + li[i][2], dp_G[i-1] + li[i][2])   # 현재 빨간색 선택한걸 더한거에서 최솟값을 구함

print(min(dp_R[N-1], dp_G[N-1], dp_B[N-1]))