from collections import deque
answer = 0


def dfs(dq, equ, target):
    global answer

    if len(dq) != 0:
        e = dq.popleft()
        dfs(dq, equ - e, target)
        dfs(dq, equ + e, target)
        dq.appendleft(e)

    else:
        if equ == target:
            answer += 1
            return answer


def solution(numbers, target):
    global answer

    dq = deque(numbers)
    dfs(dq, 0, target)

    return answer
