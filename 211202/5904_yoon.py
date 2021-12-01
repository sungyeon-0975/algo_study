import sys
# input = sys.stdin.readline


N = int(input())
# N = 11
s = 3
k = 4

while s < N:            # 다음 수열 만들기
    s = s * 2 + k
    k += 1

k -= 1                  # 위에서 편의상 더해놓은 거 빼주고
while True:
    mid = (s - k) // 2  # 중간이라기보다는 이전 수열 끝나는 지점
    if N <= mid:
        k -= 1
        s = mid
    elif mid + k < N:
        N = N - (mid + k)
        k -= 1
        s = mid
    else:
        N -= mid
        break

if N == 1:
    print('m')
else:
    print('o')