import sys
# KB / 864ms
# input = sys.stdin.readline
'''
출력 초과 => strip() 
시간 초과 => 각 문자가 어느 위치에 사용됐었는지 판단
'''

sys.stdin = open('input_6443.txt')

def dfs(idx):

    if idx == N:
        word = ''.join(sel)
        print(word)
        return

    for i in range(N):
        if not visited[i] and not used[arr[i]][idx]:
            visited[i] = 1
            sel[idx] = arr[i]
            used[arr[i]][idx] = 1  # POINT) 사용한 문자의 idx 사용 여부 1로 변경
            dfs(idx + 1)
            sel[idx] = 0
            visited[i] = 0
            if idx != N - 1:  # POINT) 마지막 순서 제외하고 다음 순서의 사용 여부 전부 0으로 초기화
                for lst in used.values():
                    lst[idx + 1] = 0

T = int(input())

for _ in range(T):
    arr = sorted(list(input().strip()))
    N = len(arr)
    visited = [0] * N  # arr에서 사용되었는지 여부
    sel = [0] * N  # 마지막에 출력할 배열
    used = {key: [0] * N for key in set(arr)}  # 각 문자별(중복x) idx에 사용되었는지 여부

    dfs(0)