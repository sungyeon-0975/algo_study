import sys
sys.stdin = open('10819_input.txt')
# input = sys.stdin.readline

# 29200KB / 196ms

def dfs(to_cal):
    global visited, answer

    if len(to_cal) == N:
        temp = 0
        for k in range(1, N):
            temp += abs(to_cal[k-1] - to_cal[k])
        if temp > answer:
            answer = temp
            return

    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            dfs(to_cal + [arr[j]])
            visited[j] = 0

N = int(input())
arr = list(map(int, input().split()))
answer = 0

for i in range(N):
    visited = [0] * N
    visited[i] = 1
    dfs([arr[i]])

print(answer)