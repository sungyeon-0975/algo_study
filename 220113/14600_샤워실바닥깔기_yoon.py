import sys
sys.stdin = open('14600_input.txt')
# input = sys.stdin.readline

# 30864KB / 72ms

def zc(i, j, half):
    for r in range(i, i+half):
        for c in range(j, j+half):
            if arr[r][c] == -1:
                return False
    return True


def tile(i, j, size):
    global num
    num += 1

    if size == 2:                       # 숫자 채우기
        for r in range(2):
            for c in range(2):
                if not arr[i+r][j+c]:
                    arr[i+r][j+c] = num
    else:
        half = size//2

        if zc(i, j, half):              # 좌상
            arr[i+half-1][j+half-1] = num
        if zc(i, j+half, half):         # 우상
            arr[i+half-1][j+half] = num
        if zc(i+half, j, half):         # 좌하
            arr[i+half][j+half-1] = num
        if zc(i+half, j+half, half):    # 우하
            arr[i+half][j+half] = num

        tile(i, j, half)
        tile(i+half, j, half)
        tile(i, j+half, half)
        tile(i+half, j+half, half)


K = int(input())
x, y = map(int, input().split())

arr = [[0] * 2**K for _ in range(2**K)]
arr[2**K-y][x-1] = -1
num = 0

tile(0, 0, 2**K)

for line in arr:
    for l in line:
        print(l, end=' ')
    print()