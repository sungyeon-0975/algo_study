import sys



c, r = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

if k > (r * c):         # 대기줄이 좌석수 초과시 바로 0 출력
    print(0)

else:
    answer = [1,0]                      # 초기 출발 좌표
    c -= 1                              # 초기에 1,0 에서 출발하므로 열이동이 처음에는 -1인 상태로 출발한다.
    variation = 1                       # 증감 여부 판단 변수

    while k > r + c:                    # 앉을 순서가 현재 행과 열에 다 앉아도 안될때
        answer[1] += variation * r      # 앉을수 있는 행 갯수만큼 y좌표 증가
        answer[0] += variation * c      # 앉을수있는열 갯수만큼 x좌표 증가


        k -= r+c                        # 남은 순서 차감, 열과 행이 하나씩 줄어듦
        r -= 1
        c -= 1
        variation *= -1                 # 증감 전환

    if k >= r:                          # 순서가 남은 행 갯수 이상인 경우
        answer[1] += variation * r
        k -= r
        answer[0] += variation * k      # 남은 순서 진행
    else:                               # 남은 행 안에 앉을 경우
        answer[1] += variation * k

    print(*answer)