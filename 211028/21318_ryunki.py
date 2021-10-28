import sys
sys.stdin = open('21318_input.txt')
"""
최적화 실패, 출력초과, 시간초과 지옥
"""
N = int(input())
data = [0]+list(map(int,input().split()))
M = int(input())
temp = [0]*(N+1)
for i in range(1,N+1):
    temp[i] += temp[i-1]

    if data[i]<data[i-1]:
        temp[i]+=1
print(temp)

for i in range(M):
    x,y = map(int,input().split())
    print(temp[y]-temp[x])