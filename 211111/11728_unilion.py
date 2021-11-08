import sys
# sys.stdin = open('11728_input.txt')
input = sys.stdin.readline

# 이게 당연히 안 될 줄 알고 밑의 방식 했는데 됐네..
# 184056KB	1584ms python
# 341388KB	1200ms pypy3
N, M = map(int, input().split())                # 배열 크기 N과 M
N_list = list(map(int, input().split()))      # 첫 번째 배열
N_list += list(map(int, input().split()))      # 두 번째 배열
print(*sorted(N_list))


# 인덱스 에러 (a 범위 늘려줘야 함) + (범위 늘리면) 메모리 초과
# N, M = map(int, input().split())                # 배열 크기 N과 M
# N_tuple = tuple(map(int, input().split()))      # 첫 번째 배열
# M_tuple = tuple(map(int, input().split()))      # 두 번째 배열
# a = 10 ** 6 + 1          # 배열 최대 길이
# temp_list = [0] * a          # 배열 저장할 리스트
# for n in N_tuple:            # 첫 배열 순회
#     temp_list[n] += 1        # 해당 인덱스에 + 1
#
# for m in M_tuple:            # 두 번재 배열 순회
#     temp_list[m] += 1        # 해당 인덱스 + 1
#
# for t in range(a//2 + 1, a):    # 중간부터 돌면서 (음수)
#     if temp_list[t]:            # 값이 있다면
#         while temp_list[t]:     # 값이 없어질 때 까지
#             print(t - a, end=" ")   # t - a출력
#             temp_list[t] -= 1       # temp_list의 해당 인덱스 - 1
#
# for tt in range(a//2 + 1):      # 처음부터 중간까지 돌면서
#     if temp_list[tt]:           # 값이 있으면
#         while temp_list[tt]:    # 값이 없어질 때 까지
#             print(tt, end=" ")  # 출력
#             temp_list[tt] -= 1  # temp_list의 해당 인덱스 - 1