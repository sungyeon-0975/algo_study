def solution(s):
    if s.count('p') + s.count('P') != s.count('y') + s.count('Y'):
        return False
    return True


print(solution('pPoooyY'))
print(solution('Pyy'))
