import sys
sys.stdin = open('1759_input.txt')
# input = sys.stdin.readline

# 30860KB / 92ms

def dfs(til, vo, con):
    global visited, answer

    if vo + con == L:
        if vo >= 1 and con >= 2:
            temp = ''.join(til)
            answer.append(temp)
        return

    idx = char.index(til[-1])
    for k in range(idx+1, C):
        if not visited[k]:
            visited[k] = 1
            if char[k] in vowel:
                dfs(til+[char[k]], vo+1, con)
            else:
                dfs(til+[char[k]], vo, con+1)
            visited[k] = 0


L, C = map(int, input().split())
char = sorted(list(map(str, input().split())))
vowel = ['a', 'e', 'i', 'o', 'u']
answer = []

for i in range(C-L+1):
    visited = [0] * C
    visited[i] = 1
    if char[i] in vowel:
        dfs([char[i]], 1, 0)
    else:
        dfs([char[i]], 0, 1)

for ans in answer:
    print(ans)