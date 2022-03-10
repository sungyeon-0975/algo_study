
NUM = [str(format(i, 'x')).upper() for i in range(16)]


def get_num(num, n):
    d, m = divmod(num, n)

    return get_num(d, n) + NUM[m] if d else NUM[m]


def solution(n, t, m, p):
    answer = ''
    num, tmp = 0, ''

    while len(tmp) <= t*m:
        tmp += get_num(num, n)
        num += 1

    for i in range(p-1, t*m, m):
        answer += tmp[i]

    return answer


print(solution(2, 4, 2, 1))
