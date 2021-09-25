import sys
sys.stdin=open('input_4013.txt')

for test in range(1,1+int(input())):
    K = int(input())
    data = [list(map(int,input().split())) for i in range(4)]


    for i in range(K):
        idx,dir = map(int,input().split())
        idx -= 1

        for i in range(idx-1,-1,-1):
            if data[i][2]!=data[i+1][6]:
                dir*=-1
