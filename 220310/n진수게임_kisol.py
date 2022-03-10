NOTATION = '0123456789ABCDEF'  # 변환용


def numeral_system(number, base):
    q, r = divmod(number, base)  # number을 base 숫자로 나눈 몫(q), 나머지(r)
    num = NOTATION[r]  # 추가할 숫자는 나머지를 변환한것

    return numeral_system(q, base) + num if q else num  # 만약 나눌게 남아있다면 재귀 호출 + num, 아니라면 그냥 num return


def solution(n, t, m, p):
    res = '0'  # 전체 배열
    answer = ''  # 튜브가 말할 숫자 배열

    x = 1
    while len(res) < t * m:  # 전체 배열은 튜브가 말할 횟수 x 사람 수와 같거나 크면됨
        res += numeral_system(x, n)
        x += 1

    for k in range(p - 1, t * m, m):
        answer += res[k]

    return answer