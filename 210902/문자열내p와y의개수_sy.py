def solution(s):
    s = s.lower()
    if s.count('p') == s.count('y'):
        return True
    else:
        return False

print(solution("pPoooyY")) #true
print(solution("Pyy")) #false