'''
첫번째 주사위를 놓으면 위의 주사위들은 자동으로 값이 정해짐
6가지의 경우의 수 -> 1 2 3 4 5 6 / 1-6 2-4 3-5

'''


import sys



index_pair = {              # 위아래가 인덱스
    0 : 5,
    1 : 3,
    2 : 4,
    3 : 1,
    4 : 2,
    5 : 0,
}

num = int(sys.stdin.readline())
dice_list = [list(map(int, sys.stdin.readline().split())) for _ in range(num)]

max_sum = 0

for idx in range(1, 7):
    tmp_sum = 0                                                     # 하나의 경우의 수에서 옆면 합을 저장하는 변수
    top = idx                                                       # 윗면의 숫자를 지정
    for dice in dice_list:
        bottom_idx = dice.index(top)                                # 아래면의 인덱스
        top_idx = index_pair.get(bottom_idx)                        # 윗면의 인덱스
        top = dice[top_idx]                                         # 윗면의 숫자
        
        tmp_idx1, tmp_idx2 = top_idx, bottom_idx                    # 슬라이싱시 인덱스로 인한 오차 발생 방지
        if tmp_idx1 > tmp_idx2:                                     # tmp_idx1 에 더 작은 숫자를 저장
            tmp_idx1, tmp_idx2 = tmp_idx2, tmp_idx1        

        tmp_sum += max(dice[:tmp_idx1] + dice[tmp_idx1+1:tmp_idx2] + dice[tmp_idx2+1:])     # 윗면과 아래면을 제외한 옆면들 중 가장 높은 수
    
    if max_sum < tmp_sum:
        max_sum = tmp_sum

print(max_sum)