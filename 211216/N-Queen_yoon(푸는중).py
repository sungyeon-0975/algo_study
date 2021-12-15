dir = [-1, 1] # j방향

def dfs(i, j, visited, n):
    global answer
    if i == n:
        answer += 1
    visited[j] = 1
    for nj in range(n):

            dfs(i+1, nj, visited, n)
    visited[j] = 0

def solution(n):
    global answer
    answer = 0
    # arr = [[0] * n for _ in range(n)]
    visited = [0] * n
    for j in range(n):
        dfs(0, j, visited, n)
    return answer

print(solution(4))