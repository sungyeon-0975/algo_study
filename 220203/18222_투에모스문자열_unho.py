import sys
import math
sys.stdin = open('input.txt')

K = int(sys.stdin.readline())           # 찾아야하는 자릿수
patterns = '0110'                       # 가장 앞의 4자리

sign = 0                                # 반전 여부
while K >= 4:                           # 4자리 이상이면 반복
    if sign:                            # 반전 여부 토글
        sign -= 1
    else:
        sign += 1

    n = int(math.log2(K))               # 현재 자릿수보다 작거나 같은 2의 제곱값 빼기
    K = K - 2**n

    if not K:                           # 0이 되면 2의 (n-1) 제곱 다시 더하기
        K = 2**(n-1)

print(int(patterns[K-1]) ^ sign)        # 초기 몇번째 자리의 값을 토글