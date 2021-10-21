import sys
# 63,544 kb, 284 ms
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())  # N: 접수창구 수, M: 정비창구 수, K: 고객 수, A: 이용한 접수 창구번호, B: 이용한 정비 창구번호
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))
    k = [0] + list(map(int, input().split()))
    a_zone = [[0, 0] for _ in range(N + 1)]  # a 접수창구 (고객번호, 접수진행상황)
    b_zone = [[0, 0] for _ in range(M + 1)]  # b 정비창구 (고객번호, 접수진행상황)
    k_finished = [1] + [0] * K  # 최종 처리 완료 여부
    k_num = [[0, 0] for _ in range(K + 1)]  # 어떤 창구 방문했는지 (접수창구번호, 정비창구번호)
    waiting_zone = []  # a와 b 사이 기다리는 곳
    res = 0  # 결과
    time = k[1]  # 제일 첫 사람의 도착시간부터 시작
    a_person = 1  # a로 들어갈 대상

    while not all(k_finished):

        for i in range(1, N + 1):
            # 접수 안했으면 접수 창구에 넣기
            if a_person < K + 1 and time >= k[a_person]:
                if a_zone[i][1] == 0:  # 접수 창구에 아무도 없으면
                    a_zone[i][0] = a_person
                    a_zone[i][1] = 1  # POINT) 들어오자마자 1부터 시작함
                    k_num[a_person][0] = i
                    a_person += 1
            # 접수 창구 -> waiting_zone으로 넣기
            if a_zone[i][1] == a[i]:
                w_person = a_zone[i][0]
                waiting_zone.append(w_person)
                a_zone[i][0], a_zone[i][1] = 0, 0  # 초기화

        for j in range(1, M + 1):
            # waiting_zone -> 정비 창구
            if b_zone[j][1] == 0 and waiting_zone:  # 정비 창구에 아무도 없으면
                b_person = waiting_zone.pop(0)  # POINT) 0번째(먼저 온 사람) pop해주기!
                b_zone[j][0] = b_person
                b_zone[j][1] = 1
                k_num[b_person][1] = j

            # 정비 창구 -> 밖으로 빠져나옴
            if b_zone[j][1] == b[j]:
                f_person = b_zone[j][0]
                k_finished[f_person] = 1  # 완료 처리
                b_zone[j][0], b_zone[j][1] = 0, 0  # 초기화

        # 시간 +1 처리
        for i in range(1, N + 1):
            if a_zone[i][0]:
                a_zone[i][1] += 1
        for j in range(M + 1):
            if b_zone[j][0]:
                b_zone[j][1] += 1
        time += 1

    for i in range(1, len(k_num)):
        if k_num[i][0] == A and k_num[i][1] == B:
            res += i

    if res:
        print('#{} {}'.format(t, res))
    else:
        print('#{} -1'.format(t))
