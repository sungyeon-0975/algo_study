from collections import defaultdict, deque


def solution(tickets):
    answer = []
    routes = defaultdict(list)
    flight = len(tickets)
    
    for s, e in tickets:
        routes[s].append(e)
    
    visited = defaultdict(list)

    for k, v in routes.items():
        v.sort()
        visited[k] = [0 for _ in range(len(v))]

    def dfs(route, cnt):
        if cnt == flight:
            return route
        
        s = route[-1]
        for idx, e in enumerate(list(routes[s])):
            if not visited[s][idx]:
                visited[s][idx] = 1
                t = dfs(route+[e], cnt+1)
                if t:
                    return t
                visited[s][idx] = 0
        
    answer = dfs(["ICN"], 0)
        
    return answer
