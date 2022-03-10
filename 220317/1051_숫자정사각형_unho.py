import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())                           # 행, 열
square = [list(sys.stdin.readline().rstrip()) for _ in range(N)]        # 입력으로 받은 사각형
answer = min(N, M)                                                      # 정사각형이므로 열과 행 중 짧은 변의 길이를 구함
end = False                                                             # 정답을 찾았는지 유무

while not end:
    for i in range(N-answer+1):                                         # 왼쪽 위에서부터 오른쪽 아래로 좌표를 탐색
        for j in range(M-answer+1):
            if square[i][j] == square[i+answer-1][j] ==\
                square[i][j+answer-1] ==square[i+answer-1][j+answer-1]: # 네개의 꼭짓점의 값이 같다면
                end = True                                              # 종료
                break
        if end:
            break
    else:
        answer -= 1

print(answer**2)            # 출력