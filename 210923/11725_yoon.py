import sys
# input = sys.stdin.readline
sys.stdin = open('input_11725.txt')

'''
47676KB / 572ms
'''


def bfs(n):
    global parent
    q = []
    q.append(n)
    while q:
        num = q.pop(0)
        nodes = tree[num]
        for node in nodes:
            if node != 1 and parent[node] == 0:
                q.append(node)
                parent[node] = num
    return parent

N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0 for _ in range(N+1)]
ans = bfs(1)[2:]
for i in range(N-1):
    print(ans[i])