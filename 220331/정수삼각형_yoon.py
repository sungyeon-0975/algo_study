def solution(triangle):
    answer = triangle[0][0]
    height = len(triangle)

    # index 같거나 +1인 경우로만 이동 가능
    dp = [0] * height
    dp[0] = triangle[0]
    for i in range(1, height):
        dp[i] = [0] * (i+1)
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif i == j:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    answer = max(dp[height-1])

    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))