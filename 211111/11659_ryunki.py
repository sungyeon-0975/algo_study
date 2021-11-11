import sys
sys.stdin = open('11659_input.txt')
"""
readline 없이 통과 불가
39468KB 280ms
"""
N,M = map(int,input().split())

data = list(map(int,input().split()))
temp = [0]
for x in range(N):
     temp.append(temp[-1]+data[x])
for _ in range(M):
    i,j = map(int,input().split())
    if i ==1:
        print(temp[j])
    else:
        print(temp[j]-temp[i-1])