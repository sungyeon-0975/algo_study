from collections import deque

def solution(n, t, m, p):                                   # 변경해야할 진법, 구해야할 정답의 개수, 게임 참여 인원, 튜브의 순서
    answer = []                                             # 정답 리스트
    turns = []                                              # 튜브가 말해야할 순서
    converted = ['0']                                       # 변경된 진법이 한자리씩 저장되는 리스트

    def convert(num):                                       # 변환 함수
        result = deque()    

        while num > 0:                                      # 0보다 크다면
            if num%n >= 10:                                 # 나머지가 10 보다 크거나 같으면
                result.appendleft(str(chr(55 + num%n)))     # 알파벳 코드값 추가
            else:                                           # 나머지가 10 보다 작다면
                result.appendleft(str(num % n))             # 숫자 추가
            num //= n

        converted.extend(result)                            # 변경된 숫자의 리스트에 추가

    for i in range(t):                      # 튜브의 말해야하는 턴을 모두 구함
        turns.append(i*m+p-1)

    num = 0
    while len(converted) <= max(turns):     # 튜브가 만들어야하는 턴까지 값을 못 구했다면
        convert(num)                        # 10진수 수를 넣어서 진번 변환
        num += 1
    
    for i in turns:                         # 튜브가 말해야 할 턴을 모두 반복
        answer.append(converted[i])         # 정답에 추가

    return ''.join(answer)

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2 ,2))