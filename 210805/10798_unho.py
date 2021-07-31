import sys

# 입력 문자열을 리스트에 담는다
str_list = [sys.stdin.readline().strip() for _ in range(5)]
answer = ''

# 입력되는 문자열의 최대 길이가 15이므로 15번 반복
# idx 는 문자열의 인덱스 값
for idx in range(15):
    # 리스트에서 각 문자열을 가져옴
    for e in str_list:
        # 인덱스 초과시 그냥 패스
        if idx >= len(e):
            continue
        
        answer += e[idx]

print(answer)