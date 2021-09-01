if __name__ == "__main__":
    dx = [0, 1, -1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    index = {0: 0}
    x, y = 0, 0
    unit = int(input())
    for _ in range(6):
        d, amount = map(int, input().split())
        x += dx[d]*amount
        y += dy[d]*amount
        if x in index.keys():
            index[x] = abs(index[x] - y)
        else:
            index[x] = y

    index = sorted(index.items())
    res = index[0][1]*(index[1][0]-index[0][0]) + index[2][1]*(index[2][0]-index[1][0])
    print(res*unit)
    
    