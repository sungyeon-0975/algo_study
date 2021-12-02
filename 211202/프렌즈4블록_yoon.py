def solution(m, n, board):
    answer = 0

    block = [[0 for _ in range(n)] for _ in range(m)]   # to list
    for i in range(m):
        for j in range(n):
            block[i][j] = board[i][j]

    clear = [[0 for _ in range(n)] for _ in range(m)]

    while True:
        go = False
        for i in range(m-1):    # pop!
            for j in range(n-1):
                if block[i][j] and block[i][j] == block[i][j+1] == block[i+1][j] == block[i+1][j+1]:
                    clear[i][j] = clear[i][j+1] = clear[i+1][j] = clear[i+1][j+1] = 1
                    go = True

        if not go:
            break

        for j in range(n):  # fill blanks
            for i in range(m):
                if clear[i][j] == 1:
                    answer += 1
                    block[i][j] = 0
                    for k in range(i, 0, -1):
                        block[k][j], block[k-1][j] = block[k-1][j], block[k][j]
                    clear[i][j] = 0

    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))