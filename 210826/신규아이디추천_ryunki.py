def solution(new_id):
    answer = ''
    check = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'
    # 1단계
    new_id = new_id.lower()

    for i in new_id:
        if i == '.' and answer[-1:]=='.': # 3단계
            continue
        elif i in check: # 2단계
            answer += i

    answer = answer.strip('.') # 4단계

    if len(answer) > 15: # 6단계
        answer = answer[:15]
        answer = answer.strip('.')

    elif len(answer) <= 2:
        if len(answer )==0: # 5단계
            answer+='a'
        while len(answer)<3: # 7단계
            answer += answer[-1]

    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
