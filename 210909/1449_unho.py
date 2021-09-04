'''
Memory - 29200 KB
Time - 80 ms
'''


import sys
sys.stdin = open('input_1449.txt')

test_case = int(input())

for _ in range(test_case):
    N, L = map(int, input().split())
    location = list(map(int, input().split()))
    location.sort(reverse=True)                     # 내림차순
    
    answer = 0                                      # 최소 테이프 갯수

    while location:
        start = location.pop()                      # 테이프를 붙일 첫 위치 
        answer += 1                                 # 테이프 하나 사용하므로 + 1

        while location and location[-1] < start+L:  # 테이프 최대 길이내에 다음 구멍이 있으면
            location.pop()                          # 막음
    
    print(answer)