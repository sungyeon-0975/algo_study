from itertools import permutations

def solution(expression):
    answer = 0                                          # 정답 변수
    op = ['*', '+', '-']                                # 연산자 기호
    _num_list = []                                      # 입력으로 주어진것에서 숫자들만 모은 리스트
    _op_list = []                                       # 연산자 리스트

    l = 0
    for r in range(len(expression)):                    # 입력으로 주어진 계산식을 숫자들과 연산자로 구분
        if not expression[r].isdigit():
            _num_list.append(int(expression[l:r]))
            _op_list.append(expression[r])
            l = r + 1
    else:
        _num_list.append(int(expression[l:]))

    for e in permutations(range(3), 3):                 # 연산자들의 우선순위를 모두 다르게 하여 반복
        num_list = _num_list.copy()                     # 숫자 리스트 복사
        op_list = _op_list.copy()                       # 연산자 리스트 복사
        cnt = 3
        idx = 0
 
        while cnt and len(num_list) > 1:                # 숫자와 연산자 리스트를 연산자 종류의 개수만큼 반복
            num_idx = 0                                 # 숫자 리스트의 인덱스
            op_idx = 0                                  # 연산자 리스트의 인덱스
            
            while num_idx < len(num_list)-1:            # 숫자들 반복
                if op_list[op_idx] == op[e[idx]]:       # 현재 우선순위가 가장 높은 연산자를 만나면 조건에 맞게 연산
                    if op[e[idx]] == '+':
                        num_list[num_idx] = num_list[num_idx] + num_list[num_idx + 1]
                    elif op[e[idx]] == '-':
                        num_list[num_idx] = num_list[num_idx] - num_list[num_idx + 1]
                    elif op[e[idx]] == '*':
                        num_list[num_idx] = num_list[num_idx] * num_list[num_idx + 1]
                    op_list.pop(op_idx)
                    num_list.pop(num_idx+1)
                else:
                    num_idx += 1        # 다음 숫자
                    op_idx += 1         # 다음 연산자
            cnt -= 1                    # 남은 반복횟수 감소
            idx += 1                    # 다음 우선순위 연산자

        answer = max(answer, abs(int(num_list[0])))     # 이전답과 비교하여 높은 값 저장


    return answer


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))