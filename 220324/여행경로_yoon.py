def solution(tickets):
    answer = []
    used = [0] * len(tickets)

    def dfs(visited, cnt):
        if cnt == len(tickets):
            answer.append(visited)
        for i in range(len(tickets)):
            if not used[i]:
                d, a = tickets[i]
                if visited[-1] == d:
                    used[i] = 1
                    dfs(visited+[a], cnt+1)
                    used[i] = 0
    dfs(["ICN"], 0)
    answer.sort()
    return answer[0]


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))