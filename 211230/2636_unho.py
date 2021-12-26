import sys
sys.stdin = open('input.txt')


def DFS(y, x):
    cheese_boundary = set()
    stack = [(y, x)]

    while stack:
        node = stack.pop()
        if not visited[node[0]][node[1]]:
            visited[node[0]][node[1]] = 1
            for k in range(4):
                r = node[0] + dr[k]
                c = node[1] + dc[k]
                
                if 0 <= r < N and 0 <= c < M and not visited[r][c]:
                    if not board[r][c]:
                        stack.append((r, c))
                    elif board[r][c]:
                        cheese_boundary.add((r, c))

    return cheese_boundary


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cheese_count = 0

hour = 0
visited = [[0] * M for _ in range(N)]
melt_cheese = DFS(0, 0)

while melt_cheese:
    hour += 1
    remain_cheese = len(melt_cheese)

    for coor in melt_cheese:
        board[coor[0]][coor[1]] = 0

    tmp = []
    for i in range(len(melt_cheese)):
        tmp.append(melt_cheese.pop())
    melt_cheese.clear()
    
    for e in tmp:
        melt_cheese.update(DFS(e[0], e[1]))

print(hour)
print(remain_cheese)