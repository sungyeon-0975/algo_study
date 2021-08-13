import sys

'''
1. 2차원 배열로 연결된 노드를 넣는다.
0번 인덱스에는 1번과 연결된 노드들
1번 인덱스에는 2번과 연결된 노드들...

2. visit node 하나 만든다
노드에 이미 방문 했다면 패스

3. 정답 리스트 (방문한 노드 차례로 쌓음)

4. 2중 반복문

'''

# dfs
def dfs_func(linked, start):
    dfs_stack = [start]
    visit_stack = []

    while dfs_stack:
        node = dfs_stack.pop()
        if node not in visit_stack:
            visit_stack.append(node)
            for e in linked[node-1]:
                dfs_stack.append(e)

    return visit_stack

# bfs
def bfs_func(linked, start):
    bfs_queue = [start]
    visit_stack = []

    while bfs_queue:
        node = bfs_queue.pop(0)
        if node not in visit_stack:
            visit_stack.append(node)
            for e in linked[node-1]:
                bfs_queue.append(e)

    return visit_stack



node, edge, start = map(int, sys.stdin.readline().split())
linked = [[] for _ in range(node)]

# 2차원 배열 - 각 노드 번호에 연결된 노드 리스트 만듦
for _ in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    linked[a-1].append(b)
    linked[b-1].append(a)

linked = list(map(lambda x: sorted(x, reverse=True), linked))

for num in dfs_func(linked, start):
    print(num, end=' ')

print()

linked = list(map(lambda x: sorted(x), linked))

for num in bfs_func(linked, start):
    print(num, end=' ')