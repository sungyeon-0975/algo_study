from collections import defaultdict, deque

def solution(tickets):
    answer = []
    gh = defaultdict(list)
    flight = len(tickets)
    
    for s, e in tickets:
        gh[s].append(e)
    
    routes = defaultdict(deque)
    for k, v in gh.items():
        routes[k] = deque(sorted(v))
    
    def dfs(route, cnt):
        nonlocal answer
        
        if cnt == flight:
            answer = route
            return
        
        s = route[-1]
        for e in list(routes[s]):
            e = routes[s].popleft()
            t =  dfs(route+[e], cnt+1)
            if t:
                return t
            
            routes[s].appendleft(e)
        
    dfs(["ICN"], 0)
        
        
        
    return answer