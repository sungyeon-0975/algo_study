def solution(n, computers):
    answer = 0
    visited = [[0] * n for _ in range(n)]
    def dfs(i):
        nonlocal answer, visited
        for j in range(n):
            if computers[i][j] == 1 and not visited[j]:
                visited[j] = 1
                dfs(j)
                visited[j] = 0
        answer += 1
    for k in range(n):
        if not visited[k]:
            dfs(k)
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))