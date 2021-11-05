"""
python
    Memory - 40 MB
    Time - 0.184 s
"""
import sys
sys.stdin = open('input.txt')


N, S = map(int, sys.stdin.readline().split())               # 길이, 부분합값 기준
li = [0] + list(map(int, sys.stdin.readline().split()))     # 숫자 리스트

for i in range(1, len(li)):         # 누적합 구하기
    li[i] = li[i-1] + li[i]
         
l, r = 0, 1         # 왼쪽, 오른쪽 인덱스
answer = 1e10       # 초기 정답 값

while r < len(li):                  # 오른쪽 인덱스 배열 범위 안에 있으면 반복
    if li[r] - li[l] >= S:          # 구간합이 기준 이상이면
        answer = min(answer, r-l)   # 정답에 있는 값과 더 작은값을 갱신
        l += 1                      # 왼쪽 인덱스 1 증가
    else:                           # 구간합이 기준 미만이면
        r += 1                      # 오른쪽 인덱스 1 증가

if answer == 1e10:      # 정답값이 초기값이면 0 반환
    print(0)
else:                   # 정답값 출력
    print(answer)