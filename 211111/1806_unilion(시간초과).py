import sys
# sys.stdin = open('1806_input.txt')
input = sys.stdin.readline

N, S = map(int, input().split())            # 수열의 길이 N, 부분합 S
N_tuple = tuple(map(int, input().split()))  # 값 변경이 안 되기에 tuple로 정의
result = N + 1      # 길이는 최대 N이기에 합이 없을 경우와 구분 위해 + 1
for i in range(N):          # 인덱스 0부터 끝까지 탐색
    # if N - i < result:    # 이건 필요없을 거 같지만
    #     break             # 시간 초과 나면 고려하기
    temp = N_tuple[i]       # temp를 N_tuple[i]로 초기화
    cnt = 1                 # cnt를 1로 초기화
    if temp >= S:           # temp가 S보다 크면
        result = cnt        # result를 cnt로 초기화
        break               # 반복문 탈출
    for j in range(i + 1, N):   # 연속된 부분합이기에 i + 1부터 시작
        temp += N_tuple[j]  # temp에 N_tuple[j] 더하기
        cnt += 1            # cnt에 1 더하기
        if result < cnt:    # cnt가 result 보다 크면 더 볼 필요 없이
            break           # 탈출

        if temp >= S:           # temp가 S 이상이면
            if result > cnt:    # result가 cnt보다 크면
                result = cnt    # result를 cnt로 초기화
            break               # 탈출
if result == N + 1:             # result가 초기 세팅 N + 1 과 같으면
    print(0)                    # 0 출력
else:                           # 그게 아니면
    print(result)               # result 출력