#시간 초과
import sys
input = sys.stdin.readline
                                                    # 처음에 리스트로 입력값들을 받았는데, 찾아보니 문자열 그대로 처리하는 게 더 빠르다고 한다.
test = input().rstrip()                             # 초기 입력 문자, 입력값을 오른쪽 공백을 제외하고 test에 넣음
test_case = int(input())                            # 테스트 케이스 갯수, 입력값을 int 형변환 후 test_case에 넣음
idx = len(test)                                     # test의 길이를 idx에 넣어줌
for _ in range(test_case):                          # test_case 만큼 반복 돌림
    edit = input()                                  # L, D, B, P 중 하나, 입력값을 edit에 넣어줌
    if edit[0] == "L":                              # 입력값이 L이면
        if idx != 0:                                # idx가 0이 아니면
            idx -= 1                                # idx를 1개 빼줌
    elif edit[0] == "D":                            # 입력값이 D이면
        if idx != len(test):                        # idx가 test의 길이, 끝 부분이 아니면
            idx += 1                                # idx를 1개 더해줌
    elif edit[0] == "B":                            # 입력값이 B이면
        if idx != 0:                                # idx가 0이 아니면
            test = test[0:idx - 1] + test[idx:]     # test에 인덱스 왼쪽 글자 삭제
            idx -= 1                                # idx를 1개 빼줌
    elif edit[0] == "P":                            # 입력값의 처음이 P이면
        test = test[0:idx] + edit[2] + test[idx:]   # test의 idx자리에 입력값의 두번째 단어를 입력
        idx += 1                                    # idx를 1개 증가시킴
print(test)                                         # test 출력


# 구글링 결과
"""
from sys import stdin
 
stk1 = list(stdin.readline().strip())
stk2 = []
n = int(input())
for line in stdin:
    if line[0] == 'L':
        if stk1: stk2.append(stk1.pop())
        else: continue
    elif line[0] == 'D':
        if stk2: stk1.append(stk2.pop())
        else: continue
    elif line[0] == 'B':
        if stk1: stk1.pop()
        else: continue
    elif line[0] == 'P':
        stk1.append(line[2])
print(''.join(stk1 + list(reversed(stk2))))
"""