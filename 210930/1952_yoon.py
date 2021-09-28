import sys
sys.stdin = open('input_1952.txt')


def pool(idx, fee):
    global min_fee

    if idx > 12: # 12월까지의 요금만 계산
        if min_fee > fee:
            min_fee = fee
        return

    # 1일권 / 1달권
    pool(idx + 1, min(fee + month[idx]*d, fee + m))
    # 3달권
    pool(idx + 3, fee + q)


T = int(input())
for t in range(1, T+1):
    d, m, q, y = map(int, input().split())
    month = [0] + list(map(int, input().split()))

    min_fee = 36000
    pool(1, 0)
    print('#{} {}'.format(t, min(min_fee, y)))