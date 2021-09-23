import sys
sys.stdin = open('input_4013.txt')


def move(num, side, direction, value):                      # 자석 번호 / 기준 대비 방향 (왼쪽, 오른쪽) / 자석 회전 방향 / 이전 자석의 접점 값
    if num < 1 or num > 4:                                  # 자석의 범위 벗어나면 자석 (1~4번까지만 있음)
        return
    elif side == 'left':                                    # 왼쪽 자석
        if value == magnetic[num][(mag_idx[num]+2)%8]:
            return
        else:
            move(num-1, 'left', (direction * -1), magnetic[num][(mag_idx[num]-2)%8])    # 다음 왼쪽 자석
    elif side == 'right':                                   # 오른쪽 자석
        if value == magnetic[num][(mag_idx[num]-2)%8]:
            return
        else:
            move(num+1, 'right', (direction * -1), magnetic[num][(mag_idx[num]+2)%8])   # 다음 오른쪽 자석
    
    mag_idx[num] += 1 * direction                           # 현재 자석의 기준 인덱스 값 이동
    



T = int(input())

for tc in range(1, T+1):
    K = int(input())
    magnetic = [[]] + [list(map(int, input().split())) for _ in range(4)]       # 각 자석 정보
    mag_idx = [0] * 5                                                           # 각 자석의 빨간 화살표 위치 인덱스
    answer = 0

    for _ in range(K):
        num, direction = map(int, input().split())

        move(num-1, 'left', direction, magnetic[num][(mag_idx[num]-2)%8])       # 왼쪽 자석
        move(num+1, 'right', direction, magnetic[num][(mag_idx[num]+2)%8])      # 오른쪽 자석
        mag_idx[num] += -1 * direction                                          # 현재 자석 인덱스 변경


    for idx in range(4):
        if magnetic[idx+1][mag_idx[idx+1]]:
            answer += 2**idx
    
    print('#{} {}'.format(tc, answer))