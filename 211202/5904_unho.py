"""
Python
    Memory - 29 MB
    Time - 0.076 s
"""


# k=0 -> 가운데 자리수 -> 각 위치별 인덱스                수열별 규칙                            수열별 총 자릿수
# k=1 -> 4 -> 0-2 3-6 7-9               s(1) 인 경우 s(0) / mooo / s(0)                 3*2+4 = 10
# k=2 -> 5 -> 0-9 10-14 15-24           s(2) 인 경우 s(1) / moooo / s(1)                10*2+5 = 25
# k=3 -> 6 -> 0-24 25-30 31-55          s(3) 인 경우 s(2) / mooooo / s(2)               25*2+6 = 56
# k=4 -> 7 -> 0-55 56-62 63-118         s(4) 인 경우 s(3) / moooooo / s(3)              56*2+7 = 119


def solution(total, i, target):          # 수열의 총 길이 / 수열의 가운데 길이 / 구하려는 자리의 인덱스(상대적)
    global answer

    if i <= 3:                  # 현재 수열이 s(0) 인 경우
        if not target:          # 현재 인덱스가 0이면 맨 앞자리 m 출력
            answer = 'm'
        else:                   # 그 외 o 출력
            answer = 'o'
        return

    side = (total-i)//2         # S(k-1) 의 길이 (현재 수열의 왼쪽/오른쪽 길이)

    if 0 <= target < side:              # 구하려는 인덱스가 왼쪽에 속할때
        solution(side, i-1, target)     # 바로 아래단계 수열로 이동
    elif side <= target < side+i:       # 구하려는 인덱스가 가운데에 속할때
        if target == side:              # 맨 앞자리이면 m
            answer = 'm'    
        else:                           # 그 외 o
            answer = 'o'
    elif side+i <= target:                      # 구하려는 인덱스가 오른쪽에 속할때
        solution(side, i-1, target-side-i)      # 인덱스를 상대적으로 다시 구함 -> 오른쪽 안에서 몇번째 인덱스인지


N = int(input())        # 입력
answer = ''

total = 3       # 수열의 총 자릿수
i = 3           # 수열 가운데에 들어갈 자릿수
while total <= N:           # 수열의 총 길이가 구하려는 자릿수보다 작으면 반복
    # print(f's({i-3}) => total(현재 수열 총 길이): {total}  //  i(현재 수열 가운데 문자의 길이): {i}')
    i += 1
    total = total*2 + i     # 다음 수열의 총 자릿수를 구함 (현재 수열 길이)*2 + 가운데 자리 길이

# print('--------------------')
# print(f'최종적으로 구해진 값 => s({i-3}) => total(총 길이): {total}  //  i(가운데 문자열의 길이): {i}')

solution(total, i, N-1)     # 현재 수열의 총 길이 / 가운데 문자열 길이 / 구하려는 인덱스(인덱스를 맞추기 위해 -1)

print(answer)











""" 메모리 초과 """
# i = 3
# while N >= len(s):
#     s = s + [0] + ([1]*i) + s
#     i += 1

# if not s[N-1]:
#     print('m')
# else:
#     print('o')