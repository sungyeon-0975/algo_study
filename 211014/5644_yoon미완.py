import sys
sys.stdin = open('input_5644.txt')

# 이동x / 상 / 우 / 하 / 좌
dir = {0:(0, 0), 1:(-1, 0), 2:(0, 1), 3:(1, 0), 4:(0, -1)}

T = int(input())
for t in range(1, T+1):
    M, A = map(int, input().split())
    am = list(map(int, input().split())) + [0]
    bm = list(map(int, input().split())) + [0]
    BC = []
    ans = 0
    for _ in range(A):
        BC.append(list(map(int, input().split())))
    BC.sort(key = lambda x:x[3], reverse=True)
    # print(BC)

    ax, ay, bx, by = 1, 1, 10, 10
    for i in range(M+1):
        select = [0, 0, 0]
        cnt = 0
        for j in range(A):
            cnt += 1
            if not select[2] and ((abs(BC[j][0] - ay) + abs(BC[j][1] - ax)) <= BC[j][2]) and ((abs(BC[j][0] - by) + abs(BC[j][1] - bx)) <= BC[j][2]):
                select[2] = BC[j][3]
            elif not select[0] and ((abs(BC[j][0] - ay) + abs(BC[j][1] - ax)) <= BC[j][2]):
                select[0] = BC[j][3]
            elif not select[1] and ((abs(BC[j][0] - by) + abs(BC[j][1] - bx)) <= BC[j][2]):
                select[1] = BC[j][3]
            else:
                cnt -= 1
            if cnt == 2:
                break
        ans += sum(select)
        ax += dir[am[i]][0]
        ay += dir[am[i]][1]
        bx += dir[bm[i]][0]
        by += dir[bm[i]][1]

    print('#{} {}'.format(t, ans))
