import sys
sys.stdin = open('input_15683.txt')

for test in range(1,1+int(input())):
    N,M = map(int,input().split())
    data=[list(map(int,input().split())) for _ in range(N)]

    start = []
    for i in range(N):
        for j in range(M):
            if data[i][j] != 0 and data[i][j]!=6:
                start.append((i,j,data[i][j]))

    print(start)

