import sys
from collections import defaultdict


tree = defaultdict(int)
t = 0
while True:
    tr = sys.stdin.readline().rstrip()
    if tr:
        tree[tr] += 1
        t += 1
    else:
        break

for tr in sorted(tree.keys()):
    print(f'{tr} {tree[tr]/t*100:.4f}')
