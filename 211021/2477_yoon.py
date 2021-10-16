import sys
sys.stdin = open('2477_input.txt')

T = int(input())
for t in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    reception = list(map(int, input().split()))
    repair = list(map(int, input().split()))
    tk = list(map(int, input().split()))

    A, B = A-1, B-1 # idx 번호 맞춰주기
    w1, w2 = [], [] # 대기목록
    p1 = 0 # 현재 rec 들어가 있는 사람 수
    rec = [None] * N
    rep = [None] * M
    mid = [0] * (K+1) # rec A칸 들어간 사람 체크용
    ans = 0

    sec = 0
    idx = 1
    while tk or p1 or w2:
        while tk and tk[0] == sec:
            tk.pop(0)
            w1.append(idx)
            idx += 1
        for i in range(N): # rec 1초씩 감소시키고 빈 자리 탐색
            if rec[i]:
                rec[i][1] -= 1
                if not rec[i][1]:
                    w2.append(rec[i][0])
                    rec[i] = None
                    p1 -= 1
            if rec[i] == None:
                if w1:
                    temp = w1.pop(0)
                    rec[i] = [temp, reception[i]]
                    p1 += 1
                    if i == A:
                        mid[temp] = 1
        for i in range(M):
            if rep[i]:
                rep[i][1] -= 1
                if not rep[i][1]:
                    rep[i] = None
            if rep[i] == None:
                if w2:
                    temp = w2.pop(0)
                    rep[i] = [temp, repair[i]]
                    if i == B and mid[temp]:
                        ans += temp
        sec += 1

    if not ans:
        ans = -1

    print('#{} {}'.format(t, ans))