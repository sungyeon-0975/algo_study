# def solution(citations):
#     target = [0] + sorted(citations,reverse=True)
#     for i in range(1, len(target)):
#         if i >= target[i]:
#             break 
#     return target[i]

def solution(citations):
    res = 0
    target = [0] + sorted(citations,reverse=True)
    for i in range(1, len(target)):
        val = min(target[i], i)
        if res < val:
             res = val
    return res


print(solution([3, 0, 6, 1, 5]))