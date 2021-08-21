def solution(new_id):
    result = ''
    
    new_id = new_id.lower()

    for i in new_id:
        if i.isalnum() or i in ['-','_','.']:
            result += i
        if len(result) >= 2 and result[-2:] == '..':
            result = result.replace('..', '.')

    if len(result) >= 2 and result[0] == '.':
        result = result[1:]
    if len(result) >= 2 and result[-1] == '.':
        result = result[:-1]
    if result == '' or result == '.':
        result = 'a'
    if len(result) >= 16:
        result = result[:15]
        if result[-1] == '.':
            result = result[:-1]
    if len(result) == 1:
        result = result*3
    elif len(result) == 2:
        result = result + result[-1]
    
    return result

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))