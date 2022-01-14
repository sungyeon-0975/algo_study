import sys
sys.stdin = open('input.txt')

def solution(n, ans):
    if n <= 0:          # 원하는 개수를 모두 구한 경우
        print(*ans)
        return
    
    for i in range(1, N+1):             # 숫자 돌아가면서 확인
        if not selected[i]:             # 숫자가 사용되었는지 확인
            selected[i] = 1             # 숫자 사용 체크
            solution(n-1, ans + [i])    # 다음 재귀 호출
            selected[i] = 0


N, M = map(int, sys.stdin.readline().split())   # 자연수 숫자, 뽑아내는 수열의 개수

selected = [0] * (N+1)          # 숫자가 선택됬는지 확인 여부

solution(M, [])                 # 재귀