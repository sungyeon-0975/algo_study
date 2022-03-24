from collections import deque


def solution(n, computers):
    answer = 0
    v = set([i for i in range(n)])
    
    for i in range(n):
        if i in v:
            v.remove(i)
            answer += 1
            dq = deque([i])
            
            while dq:
                c1 = dq.popleft()
                t = set()
                for c2 in v:
                    if computers[c1][c2]:
                        t.add(c2)
                        dq.append(c2)
                v = v-t    
    
    return answer
