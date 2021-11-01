def comb(arr, idx, n, r, k):                    # 선들이 있는 변수 리스트(line) / 선들이 있는 리스트의 위치 인덱스 / 리스트의 길이 / 선택해야하는 남은 개수 / 선택된 선들을 담는 리스트의 인덱스
    global min_x, min_y, max_x, max_y

    if idx >= n or r <= 0:                      # 선들을 모두 돌아보거나(선이 1개만 선택될수도 있음), 2개를 선택했다면
        if selected[0] and selected[1]:         # 선을 2개를 선택하였다면
            a = selected[0][0]                  # 각 값을 변수로 초기화
            b = selected[0][1]
            e = selected[0][2]
            
            c = selected[1][0]
            d = selected[1][1]
            f = selected[1][2]

            if (a*d - b*c):                     # 음수로 나누지 않으면 (분모가 음수라면 평행 또는 일치)
                x = (b*f - e*d) / (a*d - b*c)   # 주어진 식으로 교점 구하기
                y = (e*c - a*f) / (a*d - b*c)

                if x.is_integer() and y.is_integer():       # 교점이 정수라면
                    x, y = int(x), int(y)                   # 정수로 바꿈

                    if min_x >= x: min_x = x                # 가장 작은 값이나, 가장 큰 값 찾기
                    if min_y >= y: min_y = y
                    if max_x <= x: max_x = x
                    if max_y <= y: max_y = y

                    coor.add((y, x))                        # 좌표 추가
        return
    
    selected[k] = arr[idx]              # 현재 선 선택
    comb(arr, idx+1, n, r-1, k-1)       # 선을 선택했으므로 남은 선택 개수 -1개
    selected[k].clear()                 # 선 선택 정보 삭제
    comb(arr, idx+1, n, r, k)           # 선을 선택하지 않았으므로 남은 선택 개수 유지


def solution(line):
    answer = []                             # 정답 리스트

    comb(line, 0, len(line), 2, 0)          # 조합 주어진 선의 개수에서 2개를 선택함 -> nC2
    
    for i in range(max_y, min_y-1, -1):     # y좌표의 양수(+)가 위이므로, max_y 값부터 시작하여 내려옴
        tmp = ''                            # 하나의 행의 정답 담을 변수
        for j in range(min_x, max_x+1):     # x좌표는 음수(-)가 왼쪽이므로, min_x 값부터 시작하여 오른쪽으로 진행
            if (i, j) in coor:              # 현재 위치가 교점이 되는 위치이면
                tmp += '*'                  # 별 추가
            else:                           # 교점이 아니면 . 추가
                tmp += '.'
        answer.append(tmp)
        
    return answer


selected = [[], []]                                         # 선택된 선 (왼쪽 선, 오른쪽 선)
coor = set()                                                # 교점의 좌표를 저장할 집합
min_x, min_y, max_x, max_y = 1e20, 1e20, -1e20, -1e20       # 임의의 작은값, 큰값 (교점이 존재하는 가장자리 위치를 얻기 위함)


print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0]]))
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))