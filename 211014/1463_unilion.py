"""
37012KB, 616ms
"""
x = int(input())

d = [0] * (x + 1)   # 횟수를 저장
for i in range(2, x + 1):
    d[i] = d[i - 1] + 1 # 일단 1을 빼주므로 + 1

    if i % 3 == 0:  # 3으로 나누어 질 때
        d[i] = min(d[i], d[i//3] + 1)   # 1 뺀 값과 3으로 나눈 것 + 1 중 더 작은 횟수

    if i % 2 == 0:  # 2로 나누어 질 때
        d[i] = min(d[i], d[i//2] + 1)   # 1 뺀 값과 2로 나눈 것 + 1 중 더 작은 횟수

print(d[x])

# def bfs(x, con):
#     if x <= 1:
#         return con
#
#     if x % 3 == 0:
#         x //= 3
#     elif x % 2 == 0:
#         x //= 2
#     else:
#         x -= 1
#
#     con = bfs(x, con + 1)
#     return con
#
# cnt1 = bfs(x, 0)
# cnt2 = bfs(x - 1, 1)
# cnt3 = bfs(x - 2, 2)
# print(min(cnt1, cnt2, cnt3))