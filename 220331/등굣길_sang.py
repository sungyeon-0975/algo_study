def solution(m, n, puddles):
    answer = 0
    mp = [[0] * m for _ in range(n)]

    mp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if [j+1,i+1] not in puddles:
                print(i,j)
                if j>0:
                    mp[i][j] += mp[i][j-1]
                if i>0:
                    mp[i][j] += mp[i-1][j]
    answer = mp[-1][-1]  % 1000000007
    return answer


print(solution(4, 3, [[2, 2]]	))
