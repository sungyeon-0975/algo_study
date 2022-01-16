
def dfs(n, anagram):
    global l
    used = set()

    if n == l:
        print(anagram, end="\n")

    for i in range(l):
        if not visited[i] and word[i] not in used:
            visited[i] = 1
            used.add(word[i])
            dfs(n+1, anagram+word[i])
            visited[i] = 0


n = int(input())

for _ in range(n):
    word = sorted(list(input()))
    l = len(word)
    visited = [0]*l
    dfs(0, "")
