import sys
from collections import deque
sys.stdin = open('2477_input.txt')


T = int(input())
answer = []

for tc in range(1, T+1):
    N, M, K, A, B = map(int, input().split())       # 접수 창구 개수 / 정비 창구 개수 / 고객 수 / 지갑 두고간 고객 (접수 창구 번호 / 정비 창구 번호)
    reception = list(map(int, input().split()))     # 고장 접수 시간 N개
    repair = list(map(int, input().split()))        # 차량 정비 시간 M개
    K = list(map(int, input().split()))             # 고객 방문 시간
    recept_answer = []                              # 지갑 두고간 고객과 접수처 겹치는 손님들
    tc_answer = []

    elapse = -1                                                                     # 경과 시간
    task_reception, task_repair = [[] for _ in range(N)], [[] for _ in range(M)]    # 접수처, 수리처
    wait_reception, wait_repair = deque(), deque()                                  # 접수 대기줄
    end_cnt, k_idx = 0, 0         # 수리까지 모두 다 끝난 고객 카운트 / 손님 입장 인덱스

    while end_cnt < len(K):
        # 1. 손님 명단 확인 -> 손님이 0초가 되었으면 접수 대기줄에 추가
        #                     or  손님이 오는중이면 -1초

        # 2. 접수처 확인 -> 접수처가 비어 있고, 대기 손님이 있으면 접수 바로 시작
        #                   or 접수처가 비어 있고, 대기 손님 없으면 그냥 통과
        #                   or 접수 진행중인데, 0초 초과면 -1 초
        #                   or 접수 진행중인데, 0초가 되었으면 바로 수리 대기줄에 추가  (지갑 잃어버린 손님과 같으면 정답 명단에 넣기)
        
        # 3. 수리처 확인 -> 수리처가 비어 있고, 대기 손님이 있으면 바로 수리 시작
        #                   or 수리처 비어 있고, 대기 손님 없으면 그냥 통과 
        #                   or 접수 진행중인데 0초 초과면 -1초
        #                   or 수리중인데 0초가 되었으면 수리 끝냄                     (지갑 잃어버린 손님과 같으면 정답 명단에 넣기)


        for i in range(k_idx, len(K)):             # 손님 대기 명단 순회
            if not K[i]:                    # 0초가 되었으면
                k_idx += 1
                wait_reception.append(i+1)  # 접수 대기줄에 추가 (손님 번호는 1번부터이므로 +1)
            elif K[i]:                      # 손님 올 시간이 아직이면
                K[i] -= 1                   # 1초씩 마이너스


        for i in range(len(task_reception)):        # 접수처 순회
            if not task_reception[i]:               # 접수처가 비어있으면
                if wait_reception:                  # 대기 손님 있으면
                    num = wait_reception.popleft()              # 손님 접수 시작
                    task_reception[i] = [num, reception[i]-1]   # 접수 시작과 함께 바로 시간 경과
                elif not wait_reception:            # 대기 손님도 없으면 그냥 통과
                    pass

            elif task_reception[i]:                 # 접수중이면
                if task_reception[i][1]:            # 1초 이상 남았으면 
                    task_reception[i][1] -= 1       # 시간 경과
                elif not task_reception[i][1]:      # 접수 끝났으면
                    if A == i+1:                    # 접수처 번호와 지갑 두고간 접수처 번호와 같으면 (접수번호는 1번부터이므로 +1)
                        recept_answer.append(task_reception[i][0])  # 손님 번호 저장
                    wait_repair.append(task_reception[i][0])        # 손님을 수리 대기줄에 추가
                    task_reception[i] = []                          # 접수처 비움

                    if wait_reception:                              # 비웠는데, 대기줄 있으면 바로 시작
                        num = wait_reception.popleft()
                        task_reception[i] = [num, reception[i]-1]

        for i in range(len(task_repair)):           # 수리처 순회
            if not task_repair[i]:                  # 수리처가 비어있으면
                if wait_repair:                     # 대기 손님 수리 시작
                    num = wait_repair.popleft()
                    task_repair[i] = [num, repair[i]-1]
                elif not wait_repair:               # 대기 손님 없으면 통과
                    pass

            elif task_repair[i]:                    # 수리중이면
                if task_repair[i][1]:               # 1초 이상 남으면
                    task_repair[i][1] -= 1
                elif not task_repair[i][1]:         # 수리 끝났으면
                    if B == i+1 and task_repair[i][0] in recept_answer:     # 수리번호도 같고 접수 번호도 같으면 정답리스트에 추가
                        tc_answer.append(task_repair[i][0])
                    task_repair[i] = []
                    end_cnt += 1

                    if wait_repair:                 # 비웠는데, 대기줄 있으면
                        num = wait_repair.popleft()
                        task_repair[i] = [num, repair[i]-1]
    
    if not tc_answer:
        tc_answer.append(-1)
    answer.append('#{} {}'.format(tc, sum(tc_answer)))

print(*answer, sep='\n')






""" import sys
from collections import deque
sys.stdin = open('input.txt')


T = int(input())
answer = []

for tc in range(1, T+1):
    N, M, K, A, B = map(int, input().split())       # 접수 창구 개수 / 정비 창구 개수 / 고객 수 / 지갑 두고간 고객 (접수 창구 번호 / 정비 창구 번호)
    reception = list(map(int, input().split()))     # 고장 접수 시간 N개
    repair = list(map(int, input().split()))        # 차량 정비 시간 M개
    K = list(map(int, input().split()))             # 고객 방문 시간

    elapse = 0                                      # 흐른 시간
    idx_reception, idx_repair = 0, 0                # 접수 인덱스 / 정비 인덱스 (어느 사람 차례인지)
    k_idx = 0
    tc_answer = []

    task_reception, task_repair = [[0, 0] for _ in range(N)] , [[0, 0] for _ in range(M)]       # 일하는 중인 접수/정비 상황 0-사람 번호 / 1-남은 시간
    wait_reception = deque()
    wait_repair = deque()                  # 기다리는 사람들 리스트


    print(f'----- {elapse} 시작 -----')
    print(f'손님 리스트 : {K}')
    print(f'접수 대기 명단 : {wait_reception}')
    print(f'접수처 : {task_reception}')
    print(f'수리 대기 명단 : {wait_repair}')
    print(f'수리처 : {task_repair}')
    sign = False
    while True:       # 정비 모두 끝날때 까지

        for i in range(k_idx, len(K)):
            if not K[i]:
                wait_reception.append(i)
                k_idx += 1
            else:
                K[i] -= 1

        for i in range(len(task_reception)):                # 접수 리스트 확인
            if task_reception[i][1] == 1 and i == A-1:       # 지갑 두고간 고객과 접수 번호가 같으면
                tc_answer.append(task_reception[i][0] + 1)
                wait_repair.append(task_reception[i][0])
                task_reception[i] = [0, 0]
            
            elif task_reception[i][1] == 1:
                wait_repair.append(task_reception[i][0])
                task_reception[i] = [0, 0]

            elif task_reception[i][1]:
                task_reception[i][1] -= 1
            
            if len(wait_reception) > 0 and task_reception[i] == [0, 0]:
                tmp = wait_reception.popleft()
                task_reception[i] = [tmp, reception[i]]


        for i in range(len(task_repair)):                   # 정비 리스트 확인
            if task_repair[i][1] == 1 and i == B-1:          # 지갑 두고간 고객과 정비 창구 번호가 같으면
                tc_answer.append(task_repair[i][0] + 1)
                task_repair[i] = [0, 0]
                idx_repair += 1

            elif task_repair[i][1] == 1:                     # 정비 다 끝났는데, 정비 창구 번호가 다르면
                task_repair[i] = [0, 0]
                idx_repair += 1

            elif task_repair[i][1]:                         # 정비 중이면 시간 보내기
                task_repair[i][1] -= 1

            if len(wait_repair) > 0 and task_repair[i] == [0, 0]:       # 대기 손님 있고, 현재 정비가 비어 있으면
                tmp = wait_repair.popleft()                 # 대기 손님 빼고, 정비 시작
                task_repair[i] = [tmp, repair[i]]
        

        elapse += 1             # 1초가 흐름

        print(f'----- {elapse} 경과 -----')
        print(f'손님 리스트 : {K}')
        print(f'접수 대기 명단 : {wait_reception}')
        print(f'접수처 : {task_reception}')
        print(f'수리 대기 명단 : {wait_repair}')
        print(f'수리처 : {task_repair}')
        print(f'지갑 두고간 고객과 겹치는 명단 : {tc_answer}')
        
        if idx_repair >= M:
            for j in range(M):
                if task_repair[j] != [0, 0]:
                    break
            else:
                sign = True
        
        if sign:
            break

    tmp_sum = 0
    for i in range(1, len(K)+1):
        if tc_answer.count(i) == 2:
            tmp_sum += i

    if not tmp_sum:
        tmp_sum -= 1
    
    answer.append('#{} {}'.format(tc, tmp_sum))

print(*answer, sep='\n') """