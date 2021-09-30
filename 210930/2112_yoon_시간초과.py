import sys
sys.stdin = open('input_2112.txt')


def check(films):
    for j in range(W):
        same = 0
        for i in range(D-1):
            if films[i][j] == films[i+1][j]:
                same += 1
            else:
                same = 0
            if same == K-1:
                break
        if same != K-1:
            return False
    return True

def dfs(cnt, start, films):
    global ans
    if cnt >= ans:
        return
    if check(films):
        ans = cnt
        return
    if cnt == K:
        if cnt < ans:
            ans = cnt
        return
    else:
        for i in range(start, D): # 1로 들어온 애들 0으로 바꾸기
            temp = films[i][:]
            films[i] = [0] * W
            dfs(cnt+1, start+1, films)
            films[i] = temp

            temp = films[i][:] # 0으로 들어온 애들 1로 바꾸기
            films[i] = [1] * W
            dfs(cnt + 1, start + 1, films)
            films[i] = temp


T = int(input())
for t in range(1, T+1):
    D, W, K = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(D)]
    ans = K

    if K == 1:
        ans = 0
    else:
        dfs(0, 0, films)

    print('#{} {}'.format(t, ans))



# def check(films):
# for j in range(W):
#     line = ''
#     for i in range(D):
#         line += str(films[i][j])
#     if '1' * K not in line and '0' * K not in line:
#         return False
# return True