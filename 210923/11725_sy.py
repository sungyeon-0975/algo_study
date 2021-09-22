'''
실행시간 : 428ms
'''

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    tree = defaultdict(list)
    for _ in range(n-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
        
    parent = [0]*(n+1)
    parent[1] = -1
    q = deque([1])
    while q:
        now = q.popleft()
        for i in tree[now]:
            if parent[i] == 0:
                parent[i] = now
                q.append(i)

    for i in range(2, n+1):
        print(parent[i])

