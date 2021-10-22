def solution(n, wires):
    answer = n

    for i in range(len(wires)):         # 간선에서 앞에서부터 하나씩 제거를 하면서 간선이 하나씩 빠지는 모든 경우 탐색
        linked = {}                     # 노드간 연결 관계
        visited = [0] * (n+1)           # 노드간의 연결관계를 나타내기 위한 방문처리 변수

        for j in range(len(wires)): 
            if i != j:                  # 현재 간선이 제거하는 간선이 아닌 경우에
                linked[wires[j][0]] = linked.get(wires[j][0], []) + [wires[j][1]]       # 무방향 연결 관계 저장
                linked[wires[j][1]] = linked.get(wires[j][1], []) + [wires[j][0]]
        
        num = 1                     # 방문처리에 저장할 숫자 / DFS 탐색시 서로 다른 집합에 속하는것을 표현하기 위해 숫자 지정 (0-무방문, 1-첫번째 그룹, 2-두번째 그룹)
        for j in range(1, n+1):     # 노드들 하나씩 돌면서 탐색
            if not visited[j]:      # 현재 노드가 방문하지 않은 노드이면 DFS 탐색 시작
                stack = [j]

                while stack:
                    node = stack.pop()
                    if not visited[node]:       
                        visited[node] = num                 # 방문 처리 및 그룹에 속하도록 지정
                        for e in linked.get(node, []):      # 현재 노드와 연결될 노드들을 불러옴, 연결된 노드가 저장 되어 있지 않으면 빈 리스트를 반환
                            if not visited[e]:              # 방문하지 않았으면 스택에 추가
                                stack.append(e)
                
                num += 1        # 다음 그룹에 속한다고 표시를 위해, 첫번째 그룹을 다 돌고 나면 그룹 번호 숫자 증가
        
        one_cnt = visited[1:].count(1)      # 1번 그룹 개수 카운트
        two_cnt = visited[1:].count(2)      # 2번 그룹 개수 카운트

        if answer > abs(one_cnt - two_cnt):     # 그룹 개수 차이가 적으면 정답 갱신
            answer = abs(one_cnt - two_cnt)

    return answer



print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))