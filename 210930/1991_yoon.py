import sys
# input = sys.stdin.readline
sys.stdin = open('input_1991.txt')

'''
29200KB / 68ms
'''


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

for i in range(N):
    node, left, right = map(str, input().split())
    tree[node] = [left, right]

pre_order('A')
print()
in_order('A')
print()
post_order('A')