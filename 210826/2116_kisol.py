import sys

input = sys.stdin.readline

N = int(input())
nums = [[]] + [[0] + list(map(int, input().split())) for _ in range(N)]
match = {1: 6, 2: 4, 3: 5, 4: 2, 5: 3, 6: 1}  # idx 기준으로 아랫면:윗면 쌍
max_sum = 0
cnt = 0

for i in range(1, 7):  # 1번주사위의 아랫면
    dice = nums[1][:]
    temp_sum = 0
    b_idx, t_idx = i, match[i]
    b, t = dice[b_idx], dice[t_idx]
    dice[b_idx] = 0  # 리스트 안에 값
    dice[t_idx] = 0  # 리스트 안에 값
    temp_sum += max(dice)
    for j in range(2, N + 1):  # 2~N번째 주사위
        dice = nums[j][:]
        b = t
        b_idx = dice.index(b)
        t_idx = match[b_idx]
        t = dice[t_idx]
        dice[b_idx] = 0
        dice[t_idx] = 0
        temp_sum += max(dice)
        if temp_sum + (N - j) * 6 < max_sum:
            break
    if max_sum < temp_sum:
        max_sum = temp_sum

print(max_sum)
