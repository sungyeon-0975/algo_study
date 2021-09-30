import sys

# 29200KB / 72ms
# input = sys.stdin.readline
sys.stdin = open('input_1991.txt')

def pre_order(node):
    if node != '.':
        print(node, end='')
        pre_order(tree[node][0])
        pre_order(tree[node][1])


def in_order(node):
    if node != '.':
        in_order(tree[node][0])
        print(node, end='')
        in_order(tree[node][1])


def post_order(node):
    if node != '.':
        post_order(tree[node][0])
        post_order(tree[node][1])
        print(node, end='')


N = int(input())
tree = {}

for _ in range(N):
    parent, l_child, r_child = input().split()
    tree[parent] = [l_child, r_child]

pre_order('A')
print()
in_order('A')
print()
post_order('A')