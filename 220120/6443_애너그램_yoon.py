import sys
sys.stdin = open('6443_input.txt')
# input = sys.stdin.readline

# 30860KB / 1000ms


def dfs(w, cnt):
    global visited
    saved = set()
    if len(w) == cnt:
        # if w not in saved:
        #     saved.add(w)
        #     print(w)
        print(w)
    for i in range(len(word)):
        if not visited[i] and w+word[i] not in saved:
            saved.add(w+word[i])
            visited[i] = 1
            dfs(w+word[i], cnt)
            visited[i] = 0


N = int(input())
for _ in range(N):
    word = sorted(list(map(str, input().rstrip())))
    visited = [0] * len(word)
    # saved = set()
    dfs('', len(word))