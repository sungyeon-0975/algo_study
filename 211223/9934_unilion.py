import sys
input = sys.stdin.readline

def BFS(arr, x):
    mid = len(arr) // 2
    tree[x].append(arr[mid])
    if len(arr) == 1:
        return
    BFS(arr[:mid], x + 1)
    BFS(arr[mid + 1:], x + 1)

K = int(input())
N_list = list(map(int,input().split()))
tree = [[] for _ in range(K)]

BFS(N_list, 0)
for i in range(K):
    print(*tree[i])