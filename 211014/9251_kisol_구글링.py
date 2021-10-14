import sys

# KB / ms
# input = sys.stdin.readline
'''
못품 ㅠㅠ
'''
sys.stdin = open('input_9251.txt')

# 다른 사람 풀이
S1 = sys.stdin.readline().strip().upper()
S2 = sys.stdin.readline().strip().upper()
len1 = len(S1)
len2 = len(S2)
matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if S1[i - 1] == S2[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        else: matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

print(matrix[-1][-1])





def dfs(idx_B, idx_A, keyword):
    if idx_B < 0 or idx_A == 0:
        print(dp[idx_B], keyword)
        return 0
    # if dp[idx_B]:
    #     return dp[idx_B]

    if A_dict.get(B[idx_B]) and A_dict.get(B[idx_B])[-1] < idx_A:
        temp = A_dict.get(B[idx_B]).pop()
        dp[idx_B] = max(dp[idx_B], dfs(idx_B - 1, temp, A[temp] + keyword) + 1)
        A_dict.get(B[idx_B]).append(temp)
    dp[idx_B] = max(dp[idx_B], dfs(idx_B - 1, idx_A, keyword))
    return dp[idx_B]


A = input()
B = input()
A_dict = {key: [] for key in A}

for i in range(len(A)):
    A_dict[A[i]].append(i)

dp = [0] * len(B)

print(dfs(len(B) - 1, len(A), ''))
