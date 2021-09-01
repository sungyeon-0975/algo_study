import sys

input = sys.stdin.readline
# 72ms

def Warmhouse(start, sec_H, Reverse=False):
    global A

    if Reverse:
        nums.reverse()

    for i in range(1, len(nums)):
        l = nums[i][0]
        h = nums[i][1]

        if h > sec_H:
            width = abs(l - start)
            height = max_H - sec_H
            A -= width * height
            start, sec_H = l, h

        if h == max_H:
            break


N = int(input())  # 기둥 개수

# 창고 만들기
nums = [] # 창고 넓이 지정해주면 안 됨(런타임 에러ㅠㅠ)
max_H = 0  # 가장 큰 기둥 높이
for _ in range(N):
    L, H = map(int, input().split())
    nums.append((L, H))
    if max_H < H:
        max_H = H
nums.sort()

# 창고 지붕 만들기
# A(맨앞~맨뒤기둥 거리 x 가장 큰 기둥 높이) - B{(구간 별 가장 큰 기둥 높이 - 그 다음 큰 기둥 높이) x 구간 길이}
A = (nums[-1][0] - nums[0][0] + 1) * max_H

Warmhouse(nums[0][0], nums[0][1])
Warmhouse(nums[-1][0], nums[-1][1], Reverse=True)

print(A)
