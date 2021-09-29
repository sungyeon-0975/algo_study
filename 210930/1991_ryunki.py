"""

29200KB, 68ms

"""

import sys

sys.stdin = open('input_1991.txt')

def pre(start):
    if start !='.':
        print(start, end='')
        pre(tree[start][0])
        pre(tree[start][1])

def inorder(start):
    if start !='.':
        inorder(tree[start][0])
        print(start, end='')
        inorder(tree[start][1])

def post(start):
    if start !='.':
        post(tree[start][0])
        post(tree[start][1])
        print(start, end='')

N = int(input())
tree = {}

for i in range(N):
    a,b,c = input().split()
    tree[a]=[b,c]

pre('A')
print()
inorder('A')
print()
post('A')