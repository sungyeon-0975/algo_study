"""
37012KB, 604ms
"""

N = int(input())
data = [0] * (N + 1)

for i in range(2, N + 1):
    data[i] = data[i - 1] + 1
    if not i % 3:
        data[i] = min(data[i], data[i // 3] + 1)  # 더 적은 연산일 경우는 저장
    if not i % 2:
        data[i] = min(data[i], data[i // 2] + 1)
print(data[N])



