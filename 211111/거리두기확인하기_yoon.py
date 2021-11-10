di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < 5 and 0 <= nj < 5:
                        if place[ni][nj] == 'P':    # 거리 1이면 무조건 0
                            return 0
                        elif place[ni][nj] == 'O':  # 바로 옆은 0인데 그보다 한칸 더 가서 걸리면 0
                            for l in range(4):
                                if l != (k+2)%4:
                                    fi = ni + di[l]
                                    fj = nj + dj[l]
                                    if 0 <= fi < 5 and 0 <= fj < 5 and place[fi][fj] == 'P':
                                        return 0
    return 1

def solution(places):
    answer = []
    for i in range(5):
        answer.append(check(places[i]))
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))