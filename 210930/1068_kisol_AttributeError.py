import sys


# KB / ms
# input = sys.stdin.readline
'''
첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 
둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다. 만약 부모가 없다면 (루트) -1이 주어진다. 
셋째 줄에는 지울 노드의 번호가 주어진다.
'''
sys.stdin = open('input_1068(T).txt')
# sys.setrecursionlimit(10**6)


def pre_order(node):
    global cnt
    if tree.get(node):
        for child in tree[node]:
            pre_order(child)
    else:
        cnt += 1

T = int(input())

for _ in range(T):
    N = int(input())
    parents = list(map(int, input().split()))
    tree = {key: [] for key in range(0, N)}
    D = int(input())
    cnt = 0

    for i in range(1, len(parents)):
        if i == D:
            continue
        tree.get(parents[i]).append(i)

    print(parents)
    root = parents.index(-1)
    if root != D:
        pre_order(root)

    print(tree)
    print(cnt)