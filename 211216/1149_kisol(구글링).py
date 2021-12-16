import sys

# KB / ms
# input = sys.stdin.readline
'''
구글링...ㅠㅠ
'''

sys.stdin = open('input_1149.txt')

T = int(input())

for _ in range(T):
    N = int(input())
    DP = [list(map(int, input().split())) for _ in range(N)]
    # 각 색깔의 비용마다 이전에 어떤 색을 선택했을 때 가장 비용이 적게나오는지 누적해서 저장
    # i-2, i-1, i에서 i에 i-2는 영향을 주지 않음
    for i in range(1, N):
        DP[i][0] = min(DP[i - 1][1], DP[i - 1][2]) + DP[i][0]
        DP[i][1] = min(DP[i - 1][0], DP[i - 1][2]) + DP[i][1]
        DP[i][2] = min(DP[i - 1][0], DP[i - 1][1]) + DP[i][2]
    print(min(DP[N - 1][0], DP[N - 1][1], DP[N - 1][2]))