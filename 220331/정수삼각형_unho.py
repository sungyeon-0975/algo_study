def solution(triangle):
    N = len(triangle)                                   # 삼각형의 높이
    dp = []                                             # 삼각형의 높이별 나올 수 있는 값

    dp.append(triangle[0])                              # 가장 위에층 설정
    n = 1                                               # 현재 높이
    while n < N:                                        # 현재 높이가 삼각형의 높이 보다 작으면 반복
        tmp = []                                        # 현재 층의 정답 경우의 수

        tmp.append(dp[-1][0] + triangle[n][0])          # 현재 층 가장 왼쪽의 값

        for i in range(n-1):                                            # 현재 층의 양 옆을 제외하고 나올 수 있는 경우의 수
            left = dp[-1][i]                                            # 이전 층의 왼쪽 값
            right = dp[-1][i+1]                                         # 이전 층의 오른쪽 값
            plus_value = triangle[n][i+1]                               # 현재 층의 값
            tmp.append(max(left + plus_value, right + plus_value))      # 현재 층의 값에서 이전 층의 값들을 각각 더했을때 최댓값

        tmp.append(dp[-1][-1] + triangle[n][-1])        # 현재 층 가장 오른쪽 값
        dp.append(tmp)                                  # 현재 층의 경우의 수 추가
        n += 1                                          # 층 증가
            
    return max(dp[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))