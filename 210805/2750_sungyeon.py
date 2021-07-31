if __name__ == "__main__":
    n = int(input())
    l = [int(input()) for _ in range(n)]
    for i in sorted(l):
        print(i)