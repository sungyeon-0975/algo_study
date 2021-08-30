def solution(s):
    answer = True

    p_count = s.count('P') + s.count('p')
    y_count = s.count('Y') + s.count('y')

    if p_count != y_count:
        answer = False

    return answer