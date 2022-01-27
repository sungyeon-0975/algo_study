import sys
import math
from collections import deque
sys.stdin = open('input.txt')


def solution(n):
    q = deque([n])
    visited[n] = 0                      # 시작 숫자는 0번 바꿔서 돌아오므로 0으로 지정
    
    while q:
        if visited[target] < 1e10:      # 목표 숫자로 변환이 가능한 경우, 종료
            return

        node = q.popleft()
        for i in range(4):                                      # 숫자가 4자리 이므로 10의 0, 1, 2, 3 제곱을 하기 위해 4번 반복
            sign = False                                        # 자릿수 올림이 되는지 여부 변수

            for j in range(1, 10):                              # 현재 자릿수를 1부터 9까지 더하면서 바꿈
                next_number = node + 10**i*j                    # 다음 숫자는 현재 숫자의 10의 i 제곱 * j
                
                if not sign and str(next_number)[-i-1] == '0':  # 현재 변경중인 자릿수가 0이라면 올림이 발생하므로
                    sign = True                                 # 올림 여부 변수 True로 변경
                
                if sign:                                        # 올림이 발생했다면
                    next_number -= 10**(i+1)                    # 앞자리 올림 빼기

                if prime_number[next_number] and 1000 <= next_number < 10000 and visited[next_number] == 1e10:      # 소수이고, 4자리 숫자이고, 아직 확인하지 않은 숫자인 경우
                    visited[next_number] = visited[node] + 1    # 몇번 변환이 필요한지 저장
                    q.append(next_number)                       # 다음 탐색


T = int(sys.stdin.readline())                       # 테스트 케이스 개수
prime_number = [True] * 10000                       # 0 ~ 10000 숫자들의 소수 여부 판별 저장 리스트
prime_number[0], prime_number[1] = False, False     # 0과 1은 소수가 아니다

for i in range(2, int(10000**0.5)+1):               # 숫자 2부터 10000의 제곱근의 수까지 반복하여 확인
    for j in range(2, 10000//i+1):                  
        if i*j == 10000: break                      # 인덱스 에러 방지 ex) i = 2 일때, j는 5000까지 나오게 되서 인덱스가 10000 이 되는 경우를 막아야함
        prime_number[i*j] = False                   # 현재 숫자의 배수들은 모두 소수가 아니다

for _ in range(T):
    start, target = map(int, sys.stdin.readline().split())      # 시작 소수, 도착 소수
    visited = [1e10] * 10000                                    # 각 숫자로 변환을 했는지 여부

    solution(start)                 # 탐색

    if visited[target] < 1e10:      # 출력
        print(visited[target])
    else:
        print('Impossible')