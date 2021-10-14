import sys
# input = sys.stdin.readline
sys.stdin = open('input_9251.txt')

# 36252KB, 716ms

word1, word2 = input().strip(), input().strip()
dp = [[0] * (len(word1)+1) for _ in range(len(word2)+1)]
for i in range(1, len(word2)+1):
    for j in range(1, len(word1)+1):
        if word2[i-1] == word1[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])