import sys

sys.stdin = open('2477_input.txt')

for test in range(1, 1 + int(input())):
    N, M, K, A, B = map(int, input().split())
    recipt_t = list(map(int, input().split()))  # 접수시간
    maintain_t = list(map(int, input().split()))  # 정비시간
    visit_t = list(map(int, input().split()))  # 방문시간
    answer = 0

    A, B = A - 1, B - 1
    waiting_r, waiting_m = [], []
    receipt= [None] * N
    maintain = [None] * M
    end = [0] * (K + 1)
    r_t= 0
    time = 0  # 도착시간
    cnt = 1
    while visit_t or r_t :
        while visit_t and visit_t[0] == time:
            visit_t.pop(0)
            waiting_r.append(cnt)
            cnt += 1  # 번호 순서대로 넣기

        for i in range(N):
            if receipt[i]:
                receipt[i][1] -= 1
                if not receipt[i][1]:
                    waiting_m.append(receipt[i][0])
                    receipt[i] = None
                    r_t -= 1
            if receipt[i] is None:
                if waiting_r:
                    temp = waiting_r.pop(0)
                    receipt[i] = [temp, receipt[i]]
                    r_t += 1
                    if i == A:
                        end[temp] = 1

        for j in range(M):
            if maintain[j]:
                maintain[j][1] -= 1
                if not maintain[j][1]:
                    maintain[j] = None
            if maintain[j] is None:
                if waiting_m:
                    temp = waiting_m.pop(0)
                    maintain[j] = [temp, maintain_t[j]]
                    if j == B and end[temp]:
                        answer += temp
        time += 1
    if not answer:
        answer = -1
    print('#{} {}'.format(test, answer))
