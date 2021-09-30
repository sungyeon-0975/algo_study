import sys,copy
sys.stdin = open('input/2112_input.txt')

def dfs(idx, cnt):
    global res
    if cnt < res:
        if idx < d:
            dfs(idx + 1, cnt)

            membrane[idx] = [0]*w
            dfs(idx + 1, cnt + 1)

            membrane[idx] = [1]*w
            dfs(idx + 1, cnt + 1)
            membrane[idx] = mem_copy[idx][:]
        elif check():
            res = cnt
    

def check():
    for i in range(w):
        max_c = 0
        c = 1
        pre = membrane[0][i]
        for j in range(1, d):
            if membrane[j][i] == pre:
                c += 1
            else:
                if max_c < c:
                    max_c = c
                pre = membrane[j][i]
                c = 1
        if max(max_c, c) < k:
            return False
    return True



if __name__ == "__main__":
    t = int(input())
    for idx in range(1, t+1):
        d, w, k = map(int, input().split())
        membrane = [list(map(int, input().split())) for _ in range(d)]
        mem_copy = copy.deepcopy(membrane)
        res = d

        dfs(0, 0)

        print('#{} {}'.format(idx, res))

