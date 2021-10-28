def solution(n, wires):
    answer = n # 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)
    G = [[0] * (n + 1) for _ in range(n + 1)]

    # 그래프 만들기
    for a in range(n - 1):
        G[wires[a][0]][wires[a][1]] = 1
        G[wires[a][1]][wires[a][0]] = 1

    # wire마다 연결 끊기
    for i in range(n - 1):
        G[wires[i][0]][wires[i][1]] = 0
        G[wires[i][1]][wires[i][0]] = 0
        cnt = 1
        visited = [0] * (n + 1)
        stack = [1]
        visited[1] = 1

        # 그래프 순회
        while stack:
            v = stack.pop()
            for j in range(1, n + 1):
                w = G[v][j]
                if w and not visited[j]:
                    stack.append(j)
                    visited[j] = 1
                    cnt += 1

        res = abs(n - cnt * 2)
        if res < answer:
            answer = res
            if answer == 0:
                break

        G[wires[i][0]][wires[i][1]] = 1
        G[wires[i][1]][wires[i][0]] = 1

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))