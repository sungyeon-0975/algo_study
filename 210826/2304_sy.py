if __name__ == "__main__":
    n = int(input())
    pillars = []
    for i in range(n):
        pillars.append(tuple(map(int, input().split())))
    pillars.sort(key=lambda x: x[0])
    max_tuple = max(pillars, key=lambda x: x[1])
    max_idx, res = pillars.index(max_tuple), max_tuple[1]

    def find_area(start, end,  direction):
        global res
        tmp = pillars[start]
        for i in range(start, end, direction):
            if pillars[i][1] >= tmp[1]:
                res += abs(pillars[i][0]-tmp[0])*tmp[1]
                tmp = pillars[i]
    #왼쪽
    find_area(0, max_idx+1, 1)
    #오늘쪽
    find_area(n-1, max_idx-1, -1)

    print(res)

    #아래 코드를 함수사용으로 바꿈
    # tmp = pillars[0]
    # for i in range(max_idx+1):
    #     if pillars[i][1] >= tmp[1]:
    #         res += (pillars[i][0]-tmp[0])*tmp[1]
    #         tmp = pillars[i]
    # #오른쪽
    # tmp = pillars[-1]
    # for i in range(n-1, max_idx-1,-1):
    #     print(i,tmp[1], pillars[i][1])
    #     if pillars[i][1] >= tmp[1]:
    #         res += (tmp[0]-pillars[i][0])*tmp[1]
    #         tmp = pillars[i]
    
        
    

    