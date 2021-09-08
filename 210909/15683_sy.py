'''
s1 실행시간 : 3792ms
s2 실행시간 : 152ms
'''
#s1
# import copy

# def backtrack(idx):
#     global blind_spot, min_val, office
#     if idx == term:
#         if blind_spot < min_val:
#             min_val = blind_spot
#     else:
#         cctv = thing[idx]
#         for dirs in types[cctv[0]]:
#             origin = copy.deepcopy(office)
#             changed = check(dirs, cctv[1], cctv[2])
#             blind_spot -= changed
#             backtrack(idx + 1)
#             office = origin
#             blind_spot += changed


# def check(dirs, x, y):
#     global office
#     c = 0
#     for d in dirs:
#         i,j = x,y #중요
#         di,dj = temp[d][0], temp[d][1]
#         while True:
#             ni,nj = i + di, j + dj
#             if -1 < ni < n  and -1 < nj < m:
#                 i, j = ni, nj
#                 if office[i][j] == 6:
#                     break
#                 elif office[i][j] == 0:
#                     c += 1
#                     office[i][j] = '#'
#             else:
#                 break
    
#     return c


#s2
# 복사하지 않고, set으로 관리
# cctv각각의 선택방향에 따라 다 set으로 만들어 놓고 여러 cctv의 조합만 확인 하는식 -> 반복적인 계산을 줄일 수 있음

def dfs(idx, s):
    global changed
    if idx == term:
        if len(s) > changed:
            changed = len(s)
    else:
        for watched_set in thing[idx]:
            dfs(idx + 1, watched_set | s)
        
def check(dir_list, x, y):
    s = set()
    for d in dir_list:
        di, dj = temp[d][0], temp[d][1]
        ni, nj = x + di, y + dj #중요
        while -1 < ni < n  and -1 < nj < m:
            i, j = ni, nj
            if office[i][j] == 6:
                break
            elif office[i][j] == 0:
                s.add((i,j))
            ni, nj = i + di, j + dj
    return s 



if __name__ == "__main__":
    n,m = map(int, input().split())
    office = [list(map(int, input().split())) for _ in range(n)]
    temp = [(-1,0),(1,0),(0,-1),(0,1)]
    types = [ #상,하,좌,우 = 0, 1, 2, 3
        [], 
        [[0],[1],[2],[3]], 
        [[0,1],[2,3]], 
        [[0,2],[0,3],[1,2],[1,3]], 
        [[0,1,2],[1,2,3],[2,3,0],[3,0,1]], 
        [[0,1,2,3]], 
        ]

    thing = []
    blind_spot = 0
    # min_val = n*m #s1
    for i in range(n):
        for j in range(m):
            if office[i][j] == 0:
                blind_spot += 1
            elif office[i][j] != 6:
                # thing.append(office[i][j], i, j) # s1
                thing.append([check(dirs, i, j) for dirs in types[office[i][j]]])

    changed = 0
    term = len(thing)
    # backtrack(0) # s1
    dfs(0, set())
    # print(min_val) # s1
    print(blind_spot - changed)


