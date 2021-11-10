import sys
sys.stdin = open('1806_input.txt')
input = sys.stdin.readline
# 	구글링 : 40360KB 	172ms
N, S = map(int, input().split())            # 수열의 길이 N, 부분합 S
N_tuple = tuple(map(int, input().split()))  # 숫자 리스트 받기
start, end, s = 0, 0, 0                     # 시작, 끝, 합
minimum = N + 1                             # 최소 갯수
while True:
    if s >= S:
        s -= N_tuple[start]                     # 합에 start 인덱스 값 빼기
        start += 1                              # start의 위치 1 증가
        minimum = min(minimum, end - start + 1) # start~end까지가 현재 최소값보다 작으면 최소값 갱신

    else:
        if end == N:                        # end = N 되면 탐색 종료
            break
        else:
            s += N_tuple[end]               # 합에 end 인덱스 값 더하기
            end += 1                        # end + 1
if minimum == N + 1:
    print(0)
else:
    print(minimum)



# 시간 초과
# from collections import deque
#
# N, S = map(int, input().split())            # 수열의 길이 N, 부분합 S
# N_tuple = deque(map(int, input().split()))    # 숫자 리스트 받기
#
# for i in range(1, N):
#     N_tuple[i] += N_tuple[i - 1]
#
# if N_tuple[0] >= S:
#     print(1)
# else:
#     if N_tuple[N - 1] < S:
#         print(0)
#     else:
#         result = N + 1
#         for j in range(N - 1, 0, -1):
#             if N_tuple[j] - N_tuple[j - 1] >= S:
#                 result = 1
#                 break
#             if N_tuple[j] < S:
#                 break
#             else:
#                 if result > j + 1:
#                     result = j + 1
#             for k in range(j - 1, -1, -1):
#                 if j - k >= result:
#                     break
#                 if N_tuple[j] - N_tuple[k] >= S:
#                     if result > j - k:
#                         result = j - k
#                     break
#         print(result)




# 시간 초과
# N, S = map(int, input().split())            # 수열의 길이 N, 부분합 S
# N_tuple = tuple(map(int, input().split()))  # 값 변경이 안 되기에 tuple로 정의
# result = N + 1      # 길이는 최대 N이기에 합이 없을 경우와 구분 위해 + 1
# for i in range(N):          # 인덱스 0부터 끝까지 탐색
#     # if N - i < result:    # 이건 필요없을 거 같지만
#     #     break             # 시간 초과 나면 고려하기
#     temp = N_tuple[i]       # temp를 N_tuple[i]로 초기화
#     cnt = 1                 # cnt를 1로 초기화
#     if temp >= S:           # temp가 S보다 크면
#         result = cnt        # result를 cnt로 초기화
#         break               # 반복문 탈출
#     for j in range(i + 1, N):   # 연속된 부분합이기에 i + 1부터 시작
#         temp += N_tuple[j]  # temp에 N_tuple[j] 더하기
#         cnt += 1            # cnt에 1 더하기
#         if result < cnt:    # cnt가 result 보다 크면 더 볼 필요 없이
#             break           # 탈출
#
#         if temp >= S:           # temp가 S 이상이면
#             if result > cnt:    # result가 cnt보다 크면
#                 result = cnt    # result를 cnt로 초기화
#             break               # 탈출
# if result == N + 1:             # result가 초기 세팅 N + 1 과 같으면
#     print(0)                    # 0 출력
# else:                           # 그게 아니면
#     print(result)               # result 출력