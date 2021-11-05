import sys
sys.stdin = open('input.txt')


N, M = map(int, sys.stdin.readline().split())           # 배열 크기 A, B
A = list(map(int, sys.stdin.readline().split()))        # 배열 A
B = list(map(int, sys.stdin.readline().split()))        # 배열 B

l, r = 0, 0         # A 인덱스, B 인덱스
answer = []         # 정답을 담아두는 배열

while l < len(A) and r < len(B):        # A 인덱스랑 B 인덱스가 배열 범위를 모두 안벗어나면 반복
    if A[l] < B[r]:                     # A배열과 B배열 값 비교하여 A배열의 값이 더 작으면
        answer.append(A[l])             # 정답 배열에 A값 추가
        l += 1                          # A 배열 1 증가
    else:
        answer.append(B[r])             # 정답 배열에 B값 추가
        r += 1                          # B 배열 1 증가

if l == len(A):         # A 배열 값을 모두 정답에 넣었으면
    answer += B[r:]     # B 배열 남아있는거 모두 추가
else:
    answer += A[l:]

print(*answer)