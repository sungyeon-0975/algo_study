import sys

"""
29200KB 80ms
"""

# 0.5씩은 더 막아야 하니깐 양쪽을 합치면 테이프길이중에서 실제로 쓸 수 있는건 -1한 값이 된다.
sys.stdin = open('input_1449.txt')

T = int(input())

N, L = map(int, input().split())
data = list(map(int, input().split()))
data.sort()  # 무작위로 들어오는 경우 대비 실제로 빼면 오답이 나온다
answer = 0
start = 0  # 시작위치
for position in data:
    if start < position:  # 시작위치가 주어진 위치에 비해서 작은 경우는 테이프가 끝나는 길이보다 크다는 것이므로
        answer += 1  # 테이프 한번 붙인것
        start = position + L - 1  # 테이프를 새로 붙이면 그 테이프 길이의 끝지점을 시작지점으로 바꿔준다.
print(answer)

l = ['1', '+', '3']
print(''.join(l))
