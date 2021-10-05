import sys
sys.stdin = open('input_3752.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))
    visited = [1] + [0] * sum(score)
    possible = [0]
    for num in score:
        for i in range(len(possible)):
            temp = possible[i] + num
            if not visited[temp]:
                visited[temp] = 1
                possible.append(temp)
    print('#{} {}'.format(t, len(possible)))


# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     scorelist = list(map(int, input().split()))
#     pos = set()
#
#     for i in range(1 << N):
#         temp = 0
#         for j in range(N):
#             if i & (1 << j):
#                 temp += scorelist[j]
#         pos.add(temp)
#
#     print('#{} {}'.format(t, len(pos)))