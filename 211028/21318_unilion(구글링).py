import sys
input = sys.stdin.readline

# 8번 정도 도전하고도 계속 시간 초과 나서 구글링... ㅠ
# N = int(input())
# N_list = list(map(int, input().split()))
# Q = int(input())
# for q in range(Q):
#     cnt = 0
#     x, y = map(int, input().split())
#     for i in range(x - 1, y - 1):
#         if N_list[i + 1] - N_list[i] < 0:
#             cnt += 1
#     print(cnt)

# 41096KB	308ms
# 구글링
N = int(input())    # 악보 수
N_list = list(map(int, input().split()))    # 악보 난이도
temp = [0] * N  # 결과 낼 리스트
for i in range(1, N):
    if N_list[i - 1] <= N_list[i]:  # 현재 인덱스 값이 다음 인덱스 값보다 크면
        temp[i] = temp[i - 1] + 1   # temp[i]는 이전 값 + 1
    else:                           # 현재 인덱스 값이 다음 인덱스 값보다 작거나 같으면
        temp[i] = temp[i - 1]       # temp[i]는 이전 값 유지
Q = int(input())    # 질문 수
for q in range(Q):
    x, y = map(int, input().split())    # 악보 번호
    print((y - x) - (temp[y - 1] - temp[x - 1]))