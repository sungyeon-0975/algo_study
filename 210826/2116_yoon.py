import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')

def solve(idx, bottom, total):
    global res

    if idx == N:
        if total > res:
            res = total
            return
        return

    copy_arr = arr[idx][:]
    bottom_idx = arr[idx].index(bottom)
    top = arr[idx][face[bottom_idx]]
    copy_arr.remove(bottom)
    copy_arr.remove(top)
    plus = max(copy_arr)
    solve(idx+1, top, total+plus)

sys.setrecursionlimit(10**6) # 나는 오늘 재귀함수를 죽였다...
N = int(input())
face = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
arr = [list(map(int, input().split())) for _ in range(N)]
res = 0

for i in range(6): # 처음에 놓일 수 있는 주사위 면 6개
    idx = 0
    bottom = arr[idx][i]
    total = 0
    solve(0, bottom, total)

print(res)