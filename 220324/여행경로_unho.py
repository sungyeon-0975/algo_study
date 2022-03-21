def solution(tickets: list):
    answer = []                                         # 정답 리스트

    def make_linked(tickets: list):                     # 연결 관계 변수 만드는 함수
        linked = {}                                     # 연결 관계
        visited = {}                                    # 항공편 이용 여부

        for a, b in tickets:                           
            linked[a] = linked.get(a, []) + [b]         # a -> b 연결 추가
            visited[a] = visited.get(a, []) + [0]       # 항공편 방문여부 0으로 초기화
        
        for k in linked.keys():                         # 경로가 여러개인경우 사전순으로 가장 앞에 하나를 출력해야하므로
            linked[k].sort()                            # 도착지를 사전순으로 정렬

        return linked, visited
    
    linked, visited = make_linked(tickets)              # 연결 관계 변수와 방문 여부 변수 생성

    def DFS(routes):                                    # DFS 탐색 (현재까지 경로)
        if answer:                                      # 정답 경로를 찾았다면 종료
            return

        for v in visited.values():                      # 모든 항공편을 이용했는지 확인
            if not min(v):                              # 아직 이용하지 않은 항공편이 있다면 반복문 종료 후 탐색
                break
        else:                                           # 모든 항공편을 이용했다면
            answer.append(routes)                       # 정답에 추가
            return
        
        departure = routes[-1]                                              # 마지막에 도착한곳 = 현재 출발하려는 출발지
        for idx_arrival in range(len(linked.get(departure, []))):           # 출발지에서 이동 가능한 도시들 탐색
            if not visited[departure][idx_arrival]:                         # 이용하지 않은 항공편이라면
                visited[departure][idx_arrival] = 1                         
                DFS(routes + [linked[departure][idx_arrival]])              # 경로에 도착지 추가 하고 다음 경로 탐색
                visited[departure][idx_arrival] = 0

    DFS(['ICN'])                # DFS 탐색

    return answer[0]            # 경로 출력

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))                                                                                 # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]))                # ["ICN", "AOO", "BOO", "COO", "DOO", "EOO", "DOO", "COO", "BOO", "AOO"])
print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["AOO", "COO"], ["COO", "AOO"], ["BOO", "ZOO"]]))                                                                                # ["ICN", "AOO", "COO", "AOO", "BOO", "ZOO"])
print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["AOO", "BOO"], ["BOO", "AOO"], ["BOO", "FOO"], ["FOO", "COO"], ["COO", "ZOO"]]))                                                # ["ICN", "AOO", "BOO", "AOO", "BOO", "FOO", "COO", "ZOO"])
print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]))                                # ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"])
print(solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]))                                                                                # ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"])
print(solution([["ICN", "BBB"],["ICN", "CCC"],["BBB", "CCC"],["CCC", "BBB"],["CCC", "ICN"]]))                                                                                    # ["ICN", "BBB", "CCC", "ICN", "CCC", "BBB"])
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))                                                                                                                # ["ICN", "JFK", "HND", "IAD"])
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))                                                                                 # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
print(solution([["ICN", "AOO"], ["ICN", "AOO"], ["AOO", "ICN"], ["AOO", "COO"]]))                                                                                                # ["ICN", "AOO", "ICN", "AOO", "COO"])
print(solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]))                                                                                # ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"])
print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]))                                # ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"])