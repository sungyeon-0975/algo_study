def dfs(begin, target, words, visited, times):
    global temp

    if begin == target:
        temp = times
        return

    if temp < times:
        return

    for i in range(len(words)):
        if not visited[i]:
            cnt = 0
            for l in range(len(begin)):
                if begin[l] != words[i][l]:
                    cnt += 1
            if cnt == 1:
                visited[i] = 1
                dfs(words[i], target, words, visited, times+1)
                visited[i] = 0


def solution(begin, target, words):
    global temp

    answer, temp = 1e10, 1e10
    visited = [0] * len(words)

    dfs(begin, target, words, visited, 0)

    if temp == answer:
        answer = 0

    if temp < answer:
        answer = temp

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))