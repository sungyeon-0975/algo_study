def solution(n, t, m, p):
    answer = ''
    every = '0'
    i = 0
    while len(every) <= t*m:
        j = i
        temp = ''
        while j > 0:
            j, mod = divmod(j, n)
            if mod >= 10:
                temp += chr(mod + 55)
            else:
                temp += str(mod)
        every += temp[::-1]
        i += 1
    for cnt in range(t):
        answer += every[cnt * m + p - 1]
    return answer


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))