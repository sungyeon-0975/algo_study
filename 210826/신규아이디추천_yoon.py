def solution(new_id):
    answer = ''
    special = ['-', '_', '.']

    for char in new_id:
        idx = new_id.index(char)
        # 1. 대문자를 소문자로 치환
        if char.isupper():
            answer += char.lower()
        # 2. 문자제거
        elif not char.islower() and not char.isdigit() and char not in special:
            pass
        # 3. 마침표 중복 제거
        elif answer and char == '.' and answer[-1] == '.':
            pass
        else:
            answer += char

    # 3. 처음이나 끝 마침표 제거
    answer = answer.strip('.')

    # 5. 빈 문자열 처리
    if not answer:
        answer = 'a'

    # 6. 16자 이상
    if len(answer) >= 16:
        answer = answer[:15]

    # 3. 처음이나 끝 마침표 제거
    answer = answer.strip('.')

    # 7. 2자 이하
    while answer and len(answer) < 3:
        answer += answer[-1]

    return answer

print(solution('abcdefghijklmn.p'))