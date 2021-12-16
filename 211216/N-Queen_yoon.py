def dfs(i, visited, n):
    global answer
    if i == n:
        answer += 1
        return
    for j in range(n):
        visited[i] = j                              # visited(행 기준)마다 방문한 열 표시
        for pi in range(i):                         # past i(지난 행들이랑 비교했을때)
            if visited[pi] == visited[i]:           # 방문한 열이 똑같으면 break
                break
            if abs(visited[pi]-visited[i]) == i-pi: # 대각선에 위치해있으면 break
                break
        else:
            dfs(i+1, visited, n)                    # 다 통과하면 다음 행으로


def solution(n):
    global answer
    answer = 0
    visited = [0] * n
    dfs(0, visited, n)
    return answer

print(solution(4))