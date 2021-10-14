'''
628ms
'''

if __name__ == "__main__":
    s1 = '.' + input()
    s2 = '.' + input()
    dp = [[0]*len(s1) for _ in range(len(s2))]
    for i in range(1, len(s2)):
        for j in range(1, len(s1)):
            if s2[i] == s1[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp[-1][-1])

