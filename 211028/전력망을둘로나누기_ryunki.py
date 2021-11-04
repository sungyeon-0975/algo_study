def solution(n, wires):
    answer = 1e9


    def dfs(graph,start):
        stack = [start]
        cnt = 0
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node]=1
                stack.extend(graph[node])
                cnt+=1
        return cnt

    for i in range(len(wires)):
        graph = {x: [] for x in range(n + 1)}

        temp = wires[:]
        temp.remove(wires[i])
        for j in temp:
            graph[j[0]].append(j[1])
            graph[j[1]].append(j[0])


        g1,g2 = 0 , 0
        visited = [0] * n
        visited = [1] + visited
        for h in range(n+1):
            if not visited[h]:
                if not g1:
                    g1 = dfs(graph,h)
                elif not g2:
                    g2 = dfs(graph,h)
        answer = min(abs(g1-g2),answer)
    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))