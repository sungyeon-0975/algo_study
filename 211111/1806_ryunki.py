import sys
sys.stdin = open('1806_input.txt')
"""
40236KB,180ms
# """


N,S = map(int,input().split())

data = list(map(int,input().split()))

temp = [0]
for x in range(N):
     temp.append(temp[-1]+data[x])
answer = 1e9
start = 0
end = 1

while start !=N:
    if temp[end]-temp[start] >=S:
        answer = min(answer,end-start)
        start +=1
    else:
        if end !=N:
            end+=1
        else:
            start+=1
if answer == 1e9:
    print(0)
else:
    print(answer)
# temp = [data[0]]+[0]*(N-1)
# answer = 1e9
# for i in range(N):
#     for j in range(i+1,N):
#         temp[j]=temp[j-1]+data[j]
#         if temp[j]>S:
#             temp = [data[0]] + [0] * (N - 1)
#             break
#         if temp[j]==S:
#             answer = min(answer,j-i)
#
# if answer ==1e9:
#     answer = 0
# print(answer)
