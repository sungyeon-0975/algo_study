def solution(n, computers):
    answer = 0
    visited = [0] * n

    def dfs(i):
        nonlocal visited
        for j in range(n):
            if computers[i][j] == 1 and not visited[j]:
                visited[j] = 1
                dfs(j)
    for k in range(n):
        if not visited[k]:
            visited[k] = 1
            dfs(k)
            answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))