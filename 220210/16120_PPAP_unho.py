import sys
from collections import deque
sys.stdin = open('input.txt')

S = deque(sys.stdin.readline().rstrip())        # 입력 받은 문자
answer = []                                     # 한글자씩 쌓을 문자 리스트

while S:                                        # 입력 받은 문자가 아직 남아있으면 반복
    answer.append(S.popleft())                  # 가장 왼쪽 글자부터 순서대로 정답 리스트에 추가

    while len(answer) >= 4 and 'PPAP' == ''.join(answer[-4:]):      # 정답 리스트의 뒤에서부터 4글자가 PPAP 이면
        for _ in range(3):                                          # P로 변환되기 때문에 PAP 를 POP 시켜서 없앰
            answer.pop()

if ''.join(answer) == 'P':      # 정답 리스트에 P 만 남아있다면, 이 문자는 PPAP 문자이다
    print('PPAP')
else:
    print('NP')