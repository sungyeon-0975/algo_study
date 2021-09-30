'''
실행시간 : 72ms
'''

def solution(idx):
    global res
    res[0] += chr(idx + 65)
    if tree[idx][0] > 0:
        solution(tree[idx][0])
    res[1] += chr(idx + 65)
    if tree[idx][1] > 0:
        solution(tree[idx][1])
    res[2] += chr(idx + 65)

if __name__ == "__main__":
    n = int(input())
    tree = [[] for _ in range(n)]
    res = ['', '', '']
    for _ in range(n):
        a, l, r = map(lambda x: ord(x) - 65, input().split())
        tree[a] = [l, r]

    solution(0)
    
    
    print('\n'.join(res))