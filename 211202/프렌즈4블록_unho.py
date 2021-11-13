def solution(m, n, board):                  # 높이 / 가로 / 보드판
    answer = 0                              # 깨지는 블럭의 개수
    convert = [[]*n for _ in range(m)]      # 인덱스 위치별 값 변경을 위한 보드판 타입 변경
    remove = [[0]*n for _ in range(m)]      # 블럭의 부서짐 유무 저장을 위한 변수 (visited 와 유사)

    for i in range(m):                      # 문자열 -> 리스트
        convert[i] = list(board[i])
    # print(board)
    # print(convert)

    while True:                 # 더이상 부서질 불럭이 없을때까지 반복
        removable = False       # 현재 보드판 상황에서 제거될 블럭이 있는지 유무를 판단하는 변수 (매 반복시마다 값 False로 초기화)

        for i in range(m-1):        # 오른쪽, 아래로 한칸씩 하여 사각형 모양으로 깨지므로
            for j in range(n-1):    # 가장 오른쪽 열과 가장 아래 행은 순환하여 확인할 필요 없음
                if not str(convert[i][j]).isdigit():        # 현재 위치가 숫자가 아니면 (이미 제거된 블럭이 아니면)
                    character = convert[i][j]               # 현재 위치 블럭의 종류를 변수에 담음
                    if character == convert[i][j+1] and character == convert[i+1][j] and character == convert[i+1][j+1]:        # 사각형으로 블럭이 모두 같아 제거된다면
                        remove[i][j] = remove[i][j+1] = remove[i+1][j] = remove[i+1][j+1] = 1                                   # remove 변수에 각 인덱스에 맞게 1로 값 변경
                        removable = True                    # 현재 보드판 상황에서 제거되는 블럭이 있으므로 값을 true로 변경시켜줌
        
        if not removable:       # 현재 보드판이 제거될게 없으면 반복 종료
            break
        
        for j in range(n):
            for i in range(m):
                if remove[i][j]:                            # 제거 되어야 하는 블럭이라면
                    answer += 1                             # 정답 개수 증가
                    remove[i][j] = convert[i][j] = 0        # remove와 convert 값 제거
                    for k in range(i, 0, -1):                                               # 현재 위치의 블럭부터 위로 올라가며 현재 블럭이 제거되면서 생긴 빈 공간을
                        convert[k][j], convert[k-1][j] = convert[k-1][j], convert[k][j]     # 위의 블럭들이 내려오면서 자리를 채움

    return answer

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))