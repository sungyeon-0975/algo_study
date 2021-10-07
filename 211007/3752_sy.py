#통과..개빡침..scores길이 sum(s)말고 100으로 하면 runtime에러남
t = int(input())
for idx in range(1, t+1):
    n = int(input())
    s = list(map(int, input().split()))
    scores = [1] + [0]*sum(s)
    res = [0]

    for score in s:
        for i in range(len(res)):
            new = res[i] + score
            if scores[new] == 0:
                scores[new] = 1
                res.append(new)
    print('#{} {}'.format(idx, len(res)))





#시간초과
# from itertools import product
# from collections import Counter

# t = int(input())
# for idx in range(1, t+1):
#     n = int(input())
#     scores = list(map(int, input().split()))
#     res = len(set(map(sum, product(*list(map(lambda x: [x[0]*i for i in range(x[1] + 1)], Counter(scores).items()))))))
#     print('#{} {}'.format(idx, res))
    




#시간초과
# def dfs(i, acc):
#     if i == n:
#         res.add(acc)
#     else:
#         for j in range(d[keys[i]] + 1):
#             dfs(i+1, acc + keys[i]*j)

# t = int(input())
# for idx in range(1, t+1):
#     n = int(input())
#     scores = list(map(int, input().split()))
#     keys = list(set(scores))
#     n = len(keys)
#     d = {k:0 for k in keys}
#     for i in scores:
#         d[i] += 1


#     res = set()
#     dfs(0,0)

#     print('#{} {}'.format(idx, len(res)))




