import itertools

def solution(word):
    data = ['A','E','I','O','U']+list(map(list, itertools.product('AEIOU',repeat=2)))+list(map(list, itertools.product('AEIOU',repeat=3)))+list(map(list, itertools.product('AEIOU',repeat=4)))+list(map(list, itertools.product('AEIOU',repeat=5)))
    for i in range(len(data)):
        data[i] = ''.join(data[i])
    data.sort()
    return data.index(word)+1

print(solution('AAAAE'))
print(solution('AAAE'))
print(solution('I'))
print(solution('EIO'))
print(solution('UUUUU'))