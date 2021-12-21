import sys
sys.stdin = open('9934_input.txt')
# input = sys.stdin.readline

# 29200KB / 68ms

def in_order(tree, depth):
    mid = len(tree)//2
    if tree:
        in_order(tree[:mid], depth+1)
        level[depth].append(tree[mid])
        in_order(tree[mid+1:], depth+1)

K = int(input())
buildings = list(map(int, input().split()))
level = [[] for _ in range(K)]
in_order(buildings, 0)
for i in range(K):
    print(*level[i])