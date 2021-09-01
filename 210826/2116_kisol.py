import sys

input = sys.stdin.readline
# 156ms

N = int(input())
nums = [[]] + [[0] + list(map(int, input().split())) for _ in range(N)]
match = {1: 6, 2: 4, 3: 5, 4: 2, 5: 3, 6: 1}  # idx 기준으로 아랫면:윗면 쌍
max_sum = 0

for i in range(1, 7):  # 1번주사위의 아랫면
    temp_sum = 0
    t = i
    for j in range(1, N + 1):  # 1~N번째 주사위
        dice = nums[j][:]
        b_idx = dice.index(t)
        t_idx = match[b_idx]
        t = dice[t_idx]
        dice[b_idx] = dice[t_idx] = 0
        temp_sum += max(dice)

        if temp_sum + (N - j) * 6 <= max_sum:  # 남은 주사위 * 최대점수(6)을 더한게 max_sum보다 작으면 break
            break

    if max_sum < temp_sum:
        max_sum = temp_sum

print(max_sum)
