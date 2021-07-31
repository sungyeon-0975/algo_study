if __name__ == "__main__":
    t = int(input())
    dp = [[i for i in range(15)]]
    for _ in range(t):
        k = int(input())
        n = int(input())
        while len(dp) < k+1 :
            dp.append([sum(dp[-1][:i]) for i in range(1,16)])
        print(dp[k][n])


