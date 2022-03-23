def solution(n, computers):
    answer = 0
    visited = [[0] * n for _ in range(n)]
    def dfs(k):
        nonlocal answer
        if k == n:
            answer += 1
    for i in range(n):
        pass
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))