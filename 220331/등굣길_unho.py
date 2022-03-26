def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]              # 2차원 배열 생성, 누적합과 유사하여 가장 왼쪽 열과 가장 위의 행을 0으로 모두 채움

    dp[0][1] = 1                                        # 출발지 (1, 1) 에 도착 가능한 경우의 수를 1개로 만들기 위함
    for i in range(1, n+1):                             # 2차원 배열 반복
        for j in range(1, m+1):
            if [j ,i] in puddles:                       # 현재 좌표가 물에 잠긴 경우, 이 곳으로 이동이 불가능하므로 0 으로 설정
                dp[i][j] = 0
            else:                                       # 현재 좌표에 도착 가능한 경우의 수는
                dp[i][j] = dp[i-1][j] + dp[i][j-1]      # 왼쪽에서 현재 위치로 오는 경우의 수 + 위에서 현재 위치로 오는 경우의 수

    return dp[n][m] % 1000000007                        # 반환

print(solution(4, 3, [[2, 2]]))