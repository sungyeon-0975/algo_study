import sys
sys.stdin = open('input/5644.txt')

t = int(input())
dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]
for idx in range(1, t+1):
    m, a = map(int, input().split())
    A = list(map(int, input().split())) + [0]
    B = list(map(int, input().split())) + [0]
    bc = []
    res = 0
    for _ in range(a):
        bc.append(list(map(int, input().split())))
    bc.sort(key = lambda x: x[3], reverse=True)

    x1, y1, x2, y2 = 1, 1, 10, 10
    for i in range(m + 1):
        val = [0, 0, 0]
        c = 0
        for j in range(a):
            c += 1
            if val[2] == 0 and ((abs(bc[j][1] - x1) + abs(bc[j][0] - y1)) <= bc[j][2]) and ((abs(bc[j][1] - x2) + abs(bc[j][0] - y2)) <= bc[j][2]):
                val[2] = bc[j][3]
            elif  val[0] == 0 and ((abs(bc[j][1] - x1) + abs(bc[j][0] - y1)) <= bc[j][2]):
                val[0] = bc[j][3]
            elif val[1] == 0 and ((abs(bc[j][1] - x2) + abs(bc[j][0] - y2)) <= bc[j][2]):
                val[1] = bc[j][3]
            else:
                c -= 1
            if c == 2:
                break
        res += sum(val)
        x1 += dx[A[i]]
        y1 += dy[A[i]]
        x2 += dx[B[i]]
        y2 += dy[B[i]]
    
    print('#{} {}'.format(idx, res))
    




