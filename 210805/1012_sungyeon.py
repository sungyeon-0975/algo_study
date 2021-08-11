
import sys 
sys.setrecursionlimit(10000)

def solution(x,y):
    visited[y][x] = count

    if y + 1 < n : 
        if matrix[y+1][x] == 1 and visited[y+1][x] == 0 :
            solution(x,y+1)
    if y - 1 >= 0 :       
        if matrix[y-1][x] == 1 and visited[y-1][x] == 0 :
            solution(x,y-1)
    if x + 1 < m :
        if matrix[y][x+1] == 1 and visited[y][x+1] == 0 :
            solution(x+1,y)
    if x-1 >= 0 :
        if matrix[y][x-1] == 1 and visited[y][x-1] == 0 :
            solution(x-1,y)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())
        matrix = [[0]*m for _ in range(n)]
        visited =  [[0]*m for _ in range(n)]
        l=[]
        count = 0
        for _ in range(k):
            x, y = map(int, input().split())
            matrix[y][x] = 1
            l.append((x,y))

        for x,y in l:
            if visited[y][x] == 0 :
                count += 1
                solution(x,y)

        print(count)