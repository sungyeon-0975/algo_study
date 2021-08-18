if __name__ =="__main__":
    height, width = map(int, input().split())
    num = int(input())
    if num > height * width:
        print(0)
    else:
        seats = [[0]*width for _ in range(height)]
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        val = 1
        x,y,d = 0, -1, 0
        while val < num+1:
            nx = x + dx[d]
            ny = y + dy[d]
            if -1 < nx < height and -1 < ny < width and seats[nx][ny] == 0:
                seats[nx][ny] = val
                x,y = nx,ny
                val += 1
            else:
                d = (d + 1) % 4
        print(x+1, y+1)
