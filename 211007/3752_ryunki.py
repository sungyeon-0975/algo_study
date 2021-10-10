"""
69152kb, 446ms
"""

import sys
sys.stdin = open('input_3752.txt')

for test in range(1,1+int(input())):
    N = int(input())
    data = list(map(int,input().split()))

    result = set() # 중복된 수 제거 경우의 수 저장 공간
    result.add(0) # 0점은 무조건 포함된다.
    for i in range(N):
        temp = []
        for j in result: # 새롭게 갱신될 때 마다 다 더해주면 모든 경우의 수 [0,a,b,a+b,c,a+c,b+c,a+b+c]
            temp.append(data[i]+j)
        result.update(temp)

    print('#{} {}'.format(test,len(result)))

    #
    # def dfs(cnt,total):
    #     global result
    #     if cnt == N:
    #         result.add(total)
    #         return
    #     for i in range(N):
    #         if not visited[i]:
    #             visited[i]=1
    #             dfs(cnt + 1, total+data[i])
    #             dfs(cnt+1,total)
    #             visited[i]=0
