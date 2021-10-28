import sys
sys.stdin = open('1749_input.txt')

N,M = map(int,input().split())

data = list(list(map(int,input().split())) for _ in range(N))

temp = [[0]*M for _ in range(N)]

for i in range(M):
    temp[0][i]=data[0][i]

for i in range(1,N): # 밑으로만
    for j in range(M):
        temp[i][j] = temp[i-1][j] + data[i][j]
print(temp)
answer = 0
for i in range(N-1):
    for j in range(i+1,N):
        tmp = 0
        for h in range(M): # 옆으로만
            tmp2 = temp[j][h]-temp[i][h]
            tmp += tmp2 # 옆으로의 누적합 하면 다 보는거 아닌가??
            answer = max(answer,tmp)

print(answer)

