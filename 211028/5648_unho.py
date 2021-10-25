"""
추가 테스트 케이스 답
#1 24
#2 0
#3 6
#4 10
#5 10
#6 3
#7 8
#8 17
#9 16
#10 10
#11 7
#12 1111

구현

Memory - 79936 kb
Time - 7595 ms
"""



import sys
sys.stdin = open('5648_input.txt')


dr = [1, 0, -1, 0]          # 방향 (상 우 하 좌)
dc = [0, 1, 0, -1]

T = int(input())
answer = []

for tc in range(1, T+1):
    N = int(input())
    atoms = {}                  # 원자들 정보 (키 - 현재 원자 위치의 좌표 / 값 - 원자의 진행방향, 에너지)
    tc_answer = 0               # 폭발하는 경우의 에너지 총합

    for _ in range(N):
        x, y, direction, energe = map(int, input().split())     # 각 원자들의 정보 (좌표, 진행 방향, 에너지)

        if direction == 1: direction = 2            # 편의를 위한 원자들 진행 방향 보정
        elif direction == 2: direction = 3
        elif direction == 3: direction = 1

        atoms[(y, x)] = [(direction, energe)]       # 원자들 정보에 추가, (키-좌표 / 값-진행방향, 에너지) - 하나의 좌표에 여러 원자가 쌓일 수 있도록 값은 스택처럼 쌓이게 됨
    
    # print(f'----- 원자의 개수 : {N}')
    # for k, v in atoms.items():
    #     print(f'원자 위치 {k} - 속성 {v}')

    idx = 2000                              # 두개의 원자가 가장 끝에서 시작하는 경우 ((1000,0) 과 (-1000,0) 인 경우 최악의 경우 2000초 후에 충돌)
    while idx >= 0:                         # 시간이 다 될때까지 반복 (딕셔너리에 값이 남았는지 판단할 경우, 판단하는데 시간이 오래 걸려서 넣지 않는게 좋음

        remove = []                         # 0.5초 후에 충돌하여 폭발하는 경우를 추가하는 리스트

        keys = list(atoms.keys())                   # 처음에 좌표값을 모두 반복하여 진행할 방향에 이미 원자가 있는지 여부 파악 (0.5초 후에 충돌하는 경우 탐지를 위함)
        for k in keys:
            y, x = k

            r = y + dr[atoms[(y, x)][0][0]]
            c = x + dc[atoms[(y, x)][0][0]]

            if atoms.get((r, c)) and (atoms[(y, x)][0][0]+2) % 4 == atoms[(r,c)][0][0]:     # 바로 옆에 원자가 있는데, 진행하는 방향이 서로 마주보는 경우
                remove.append((y, x))                                                       # 현재 좌표 제거 명단에 추가
        
        if remove:                              # 0.5초후 폭발할 좌표들이 있다면
            for e in remove:                    
                tc_answer += atoms[e][0][1]     # 해당 좌표의 에너지를 추가 시킴
                atoms.pop(e)                    # 이제 원자는 필요없으므로 좌표 및 정보 제거
        
        keys = list(atoms.keys())               # 원자들 한칸씩 이동
        for k in keys:
            y, x = k

            r = y + dr[atoms[k][0][0]]
            c = x + dc[atoms[k][0][0]]

            if -1000 <= r <= 1000 and -1000 <= c <= 1000:                   # 원자들이 범위를 벗어나지 않으면
                atoms[(r, c)] = atoms.get((r, c), []) + [atoms[k][0]]       # 새로 이동할 좌표에 정보 추가 (여러개의 원자가 한곳에 모일 경우 스택처럼 쌓임)
            atoms[k].pop(0)                                                 # 기존에 있던 좌표의 정보는 제거

        keys = list(atoms.keys())       # 한곳에 만나게된 원자들 폭발
        for k in keys:
            if len(atoms[k]) > 1:                       # 정보가 여러개 있다면 (다수의 원자가 한곳에 모여있다면)
                # for k, v in atoms.items():
                #     print(f'time : {idx}')
                #     print(f'원자 위치 {k} - 속성 {v}')
                #     print(f'{tc_answer}')
                while atoms[k]:                         # 모인 모든 원자들 폭발
                    tc_answer += atoms[k].pop()[1]
                atoms.pop(k)                            # 모두 폭발했으므로 정보에서 제거
            elif len(atoms[k]) == 0:                    # 현재 좌표에 원자가 없는 경우 좌표 제거
                atoms.pop(k)
        

        idx -= 1

    answer.append('#{} {}'.format(tc, tc_answer))
print(*answer, sep='\n')