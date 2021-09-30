'''
실행시간 : 4104ms
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solution(l):
    if l:
        root_val = l[0]
        idx = -1
        for i in range(1, len(l)):
            if l[i] > root_val:
                idx = i
                break
        if idx == -1:
            solution(l[1:])
        else:
            solution(l[1:idx])
            solution(l[idx:])
        print(root_val)

if __name__ == "__main__":
    l = []
    while True:
        try:
            l.append(int(input()))
        except:
            break

    solution(l)
    
    