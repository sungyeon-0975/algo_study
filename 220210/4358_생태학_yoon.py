import sys
sys.stdin = open('4358_input.txt')
# input = sys.stdin.readline

# 111392KB / 432ms

trees = {}
for tree in sys.stdin.read().rstrip().split('\n'):
    if trees.get(tree, 0):
        trees[tree] += 1
    else:
        trees[tree] = 1

all = sum(trees.values())

for tree in sorted(trees.keys()):
    print(f'{tree} {trees[tree]/all*100:.4f}')