import sys

sys.stdin = open('input.txt')


# 마주볼때 옆면의 최댓값들의 합?
import sys
input = sys.stdin.readline
def max_sum(data):
    result = [] # 경우의 수들을 저장하는 리스트
    for j in range(6): # 첫 주사위를 각 면을 빼면서 옆면들의 최댓값을 구하는 반복
        msum = 0
        dice = data[0][:] # 받아온 주사위 첫번째의 복사
        bottom = dice[j] # 밑면
        top = dice[match[j]] # 윗면
        dice.remove(bottom) # 둘을 제거해주고
        dice.remove(top)
        msum += max(dice) # 최댓값을 합에 더한다.
        for h in range(1, N): # 나머지 주사위들을 밑면 주사위기준으로 쌓으면서 확인
            dice = data[h][:]
            bottom = top
            top = dice[match[dice.index(bottom)]]
            dice.remove(bottom)
            dice.remove(top)
            msum += max(dice)

        result.append(msum) # 합들의 저장

    return max(result) # 그 합의 맥스


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
match = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

answer = max_sum(data)
print(answer)
