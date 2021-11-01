from collections import deque
def solution(k, dungeons):
    n = len(dungeons)
    cnt = 0
    q = deque()
    q.append([k, []])
    while q:
        power, v = q.popleft()
        for i in range(n):
            mp, ap = dungeons[i]
            if i not in v and power >= mp and power >= ap:
                q.append([power - ap, v + [i]])
            else:
                cnt = max(cnt, len(v))
    return cnt

print(solution(80, [[80,20],[50,40],[30,10]]))