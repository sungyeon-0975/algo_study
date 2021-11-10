import sys
# sys.stdin = open('11659_input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())            # 수의 갯수, 예시 케이스
N_list = list(map(int, input().split()))    # 수 리스트
for i in range(1, N):                       # N_list를 돌면서 이전 꺼를 더해 나가기
    N_list[i] += N_list[i - 1]
for _ in range(M):                          # 예시 케이스 돌면서
    i, j = map(int, input().split())        # 인덱스 두 숫자를 받고
    if i != 1:                              # i가 1이 아니면
        print(N_list[j - 1] - N_list[i - 2])    # j - 1에서 i - 2 값 뺀 값 출력
    else:                       # i가 1이면
        print(N_list[j - 1])    # j - 1 값 출력