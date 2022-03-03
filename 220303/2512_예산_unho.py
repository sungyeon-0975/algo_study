import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())                           # 예산 요청의 개수
nums = list(map(int, sys.stdin.readline().split()))     # 예산 요청 금액들
government = int(sys.stdin.readline())                  # 정부의 총 예산

answer = 0                      # 최대 상한액
low, high = 0, max(nums)        # 최솟값 0, 최댓값은 예산 요청의 최대액

while low <= high:              # 이분탐색
    mid = (low+high) // 2       # 현재 상한액

    tmp_sum = 0                 # 상한액 이하로 받게끔 하였을때, 정부에 요청하는 총 예산
    for num in nums:
        if mid <= num:          # 상한액 이상을 요청하면, 상한액만 요청 가능하도록 설정
            tmp_sum += mid
        else:                   # 상한액 이하 요청이면, 요청한 금액 그대로
            tmp_sum += num

    if tmp_sum > government:    # 정부 예산을 초과하면 상한액을 더 낮춤
        high = mid - 1
    else:                       # 정부 예산 초과 안하면 상한액을 조금 더 높임
        low = mid + 1
        answer = mid

print(answer)