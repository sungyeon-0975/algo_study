import sys

# 57112KB / 376ms
# input = sys.stdin.readline
'''

'''
sys.stdin = open('input_21318.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    Q = int(input())
    questions = [list(map(int, input().split())) for _ in range(Q)]
    Q_level = [0] * (N + 1)  # 누적으로 높은 난이도가 나온 횟수 저장

    # 1~마지막에서 두번째값
    for i in range(1, N):
        Q_level[i] = Q_level[i - 1]
        if arr[i] > arr[i + 1]:
            Q_level[i] += 1
    # 마지막 값
    Q_level[N] = Q_level[N - 1]

    # 실수 개수 출력
    for i in range(Q):
        s, e = questions[i][0] - 1, questions[i][1] - 1
        print(Q_level[e] - Q_level[s])
