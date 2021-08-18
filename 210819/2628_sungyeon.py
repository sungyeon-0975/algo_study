if __name__ == "__main__":
    width, height = map(int, input().split())
    vertical, horizontal = [0,width], [0,height]
    for _ in range(int(input())):
        a,b = map(int, input().split())
        if a == 0:
            horizontal.append(b)
        else:
            vertical.append(b)
    vertical.sort()
    horizontal.sort()
    max_width, max_height = 0, 0
    for i in range(1, len(horizontal)):
        max_height = max(max_height, horizontal[i] - horizontal[i-1])
    for i in range(1, len(vertical)):
        max_width = max(max_width, vertical[i] - vertical[i-1])

    print(max_width*max_height)