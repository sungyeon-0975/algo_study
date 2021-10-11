"""
DP 가 아직 익숙치 않아서 구글링 하면서 코딩했습니다.
29708KB, 80ms
"""
import sys
input = sys.stdin.readline
n = int(input())
n_list = []     # 현재 포도주 양
for _ in range(n):
    n_list.append(int(input()))

d = [0] * n # 포도주 양
try:    # 포도주가 3개 이하일 수 있다.
    d[0] = n_list[0]           # d[0]은 처음 포도주 양
    d[1] = n_list[0] + n_list[1]    # d[1]은 처음과 두 번째 포도주 합
    d[2] = max(n_list[0] + n_list[1], n_list[0] + n_list[2], n_list[1] + n_list[2])
    # d[2]는 이전 2개의 합, 2번째 전과 자신의 합, 전과 자신의 합 중 가장 큰 것

    for i in range(3, n):
        d[i] = max(d[i - 2] + n_list[i], d[i - 3] + n_list[i - 1] + n_list[i], d[i - 1])
        # d[i]는 2번째 전과 자신의 합, 3번째 전과 이전과 자신의 합, 자신은 안 마시는 경우 중 가장 큰 값
except:
    pass    # 포도주가 3개 이하일 때 패스
finally:
    print(max(d))   # d 값 중 가장 큰 값 출력