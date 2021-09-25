""" 
Memory - 29200 KB (28.52 MB)
Time - 76 ms
"""

import sys
sys.stdin = open('input_1991.txt')


# 전위 순회
def pre_order(node):
    if node == '.':
        return

    answer[0].append(node)
    pre_order(tree[node][0])
    pre_order(tree[node][1])


# 중위 순회
def in_order(node):
    if node == '.':
        return

    in_order(tree[node][0])
    answer[1].append(node)
    in_order(tree[node][1])


# 후위 순회
def post_order(node):
    if node == '.':
        return

    post_order(tree[node][0])
    post_order(tree[node][1])
    answer[2].append(node)



N = int(input())

tree = {}
answer = [[], [], []]


for _ in range(N):
    parent, left, right = input().strip().split()
    tree[parent] = tree.get(parent, [left, right])

pre_order('A')
in_order('A')
post_order('A')

for idx in range(3):
    print(''.join(answer[idx]))