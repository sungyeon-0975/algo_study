import sys
sys.stdin=open('2383_input.txt')
"""
완전탐색
계단마다 걸리는 시간 계산
넣는 스택을 한정하면 되려나
"""

for test in range(1,1+int(input())):
    N = int(input())
    data = list(list(map(int,input().split())) for _ in range(N))
    people = []
    stair = []
    for i in range(N):
        for j in range(N):
            if data[i][j]==1:
                people.append((i,j))
            elif data[i][j]>=2:
                stair.append((i,j,data[i][j]))

