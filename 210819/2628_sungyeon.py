if __name__ == "__main__":
    width, height = map(int, input().split())
    vertical, horizontal = [0,width], [0,height]
    for _ in range(int(input())):
        a,b = map(int, input().split())
        if a == 0:
            horizontal.append(b)
        else:
            vertical.append(b)

    def find_max_len(l):
        l.sort()
        max_len = 0
        for i in range(1, len(l)):
            max_len = max(max_len, l[i] - l[i-1])
        return max_len

    print(find_max_len(vertical) * find_max_len(horizontal))