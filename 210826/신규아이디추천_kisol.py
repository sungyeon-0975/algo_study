import sys

input = sys.stdin.readline


def solution(new_id):
    id = list(new_id)
    possible = ['-', '_', '.']
    answer = ''

    # 1단계(대문자->소문자), 2단계(허용문자 외 제거)
    for char in id:
        if char.isupper():
            answer += char.lower()
        elif char.islower() or char.isdigit() or char in possible:
            answer += char

    # 3단계(..->.)
    while '..' in answer:
        answer = answer.replace('..', '.', answer.count('..'))

    # 4단계(.이 처음이나 마지막에 있을 때 제거)
    answer = answer.strip('.')

    # 5단계(비어있으면 a 삽입)
    if not answer:
        answer += 'a'

    # 6단계(길이>=16자이면 첫 15자까지만 가져오기 .이 마지막에 있으면 또 제거)
    answer = answer[:15].strip('.')

    # 7단계(2자 이하면 마지막 문자를 3자 이상이 될 때까지 끝에 반복)
    while len(answer) < 3:
        answer += answer[-1]

    return answer


print(solution('...!@BaT#*..y.abcdefghijklm'))
print(solution('z-+.^.'))
print(solution('=.='))
print(solution('123_.def'))
print(solution('abcdefghijklmn.p'))
