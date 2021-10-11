"""
36252KB, 724ms
구글링 하면서 겨우 이해함...
DP 생각보다 진짜 어려운 것..
"""
A = input()
B = input()

LCS = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
for i in range(len(A) + 1):
    for j in range(len(B) + 1):
        if i == 0 or j == 0:    # 인덱스를 맞추기 위해 한 칸 띄움
            LCS[i][j] = 0
        elif A[i - 1] == B[j - 1]:  # 해당 문자가 추가되기 이전의 LCS 길이 + 1
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:   # 문자의 인덱스가 다를 때는 이전의 LCS 최대 길이를 유지, ex) AB와 GBC => A와 GBC, AB와 GB 중 LCS 최댓값
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

print(LCS[len(A)][len(B)])