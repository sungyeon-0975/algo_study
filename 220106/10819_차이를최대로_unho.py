import sys
sys.stdin = open('input.txt')


def DFS(n, pre, ans):                                       # 숫자를 선택한 횟수, 이전에 선택한 값, 지금까지 계산한 결과 값
    global answer

    if n >= N-1 and answer < ans:                           # 모든 숫자들을 계산하고, 계산 결과가 최댓값일때
        answer = ans                                        # 정답 갱신
        return

    for i in range(N):                                      # 숫자 리스트 반복
        if not selected[i]:                                 # 아직 사용하지 않은 숫자이면
            selected[i] = 1                                 # 사용 처리
            DFS(n+1, num_li[i], ans + abs(pre - num_li[i])) # 재귀 호출 (사용 개수 추가, 현재 값, 이전값-현재값의 절대값)
            selected[i] = 0                                 # 사용 되돌리기
             
            
N = int(sys.stdin.readline())                               # 숫자 개수
num_li = list(map(int, sys.stdin.readline().split()))       # 숫자 리스트
selected = [0] * N                                          # 숫자 사용 여부 리스트

answer = 0

for i in range(N):              # 첫번째 숫자 반복
    selected[i] = 1
    DFS(0, num_li[i], 0)        # DFS 함수 호출
    selected[i] = 0

print(answer)                   # 출력