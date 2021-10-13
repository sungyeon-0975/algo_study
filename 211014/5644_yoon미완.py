import sys
sys.stdin = open('input_5644.txt')

# 이동x / 상 / 우 / 하 / 좌
dir = {0:(0, 0), 1:(-1, 0), 2:(0, 1), 3:(1, 0), 4:(0, -1)}

def check(a, b, step, temp):
    global charge
    if step > M:
        charge = temp
        return
    ai, aj = a
    bi, bj = b
    na = (ai+dir[am[step]][0], aj+dir[am[step]][1])
    nb = (bi+dir[bm[step]][0], bj+dir[bm[step]][1])
    # print(temp)
    check(na, nb, step+1, temp + BC[arr[a[0]][a[1]]] + BC[arr[b[0]][b[1]]])


T = int(input())
for t in range(1, T+1):
    M, A = map(int, input().split())
    am = list(map(int, input().split()))
    bm = list(map(int, input().split()))
    arr = [[0] * 11 for _ in range(11)]
    # print(arr)
    BC = [0]
    charge = 0
    for idx in range(1, A+1):
        i, j, cov, p = map(int, input().split())
        for r in range(1, 11):
            for c in range(1, 11):
                if abs(r + c - i - j) <= cov:
                    arr[r][c] = cov
        BC.append(p)
    # print(arr)
    a, b = (1, 1), (10, 10)
    check(a, b, 0, 0)
    print(charge)