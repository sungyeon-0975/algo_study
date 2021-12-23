import sys

# 29200KB / 68ms Python3
# input = sys.stdin.readline
'''

'''

sys.stdin = open('input_9934.txt')


def in_order(node, k):  # (root의 node 번호, level 들어갈 때 빼줄 2**k에서 지수)
    if 0 <= node < max_node:  # node 번호가 0~마지막 번호 사이면
        if k >= 0:  # 마지막 단계 0 이상이면
            in_order(node - 2 ** k, k - 1)  # 왼쪽 일때는 2 ** k를 빼주고, level이 들어가니까 -1 처리
        tree[k + 1].append(arr[node])  # 각 레벨에 빌딩 번호 추가
        if k >= 0:
            in_order(node + 2 ** k, k - 1)


T = int(input())

for _ in range(T):
    K = int(input())
    arr = list(map(int, input().split()))
    max_node = 2 ** K
    root = (max_node - 1) // 2
    tree = [[] for _ in range(K)]  # 각 level별로 빌딩 번호 저장할 tree

    in_order(root, K - 2)

    for i in range(K - 1, -1, -1):  # 역순으로 출력
        print(*tree[i])
