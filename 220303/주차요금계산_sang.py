from collections import defaultdict


def cal_time(t1: str, t2: str):
    h1, m1 = t1.split(":")
    h2, m2 = t2.split(":")

    return (int(h2)-int(h1)) * 60 + (int(m2)-int(m1))


def solution(fees, records):
    answer = []
    parking_record = defaultdict(str)
    fee_record = defaultdict(int)

    for record in records:
        t, n, _ = record.split()

        if n in parking_record:
            t1 = parking_record[n]
            tmp_time = cal_time(t1, t)
            fee_record[n] += tmp_time
            parking_record.pop(n)

        else:
            parking_record[n] = t

    for n, t in parking_record.items():
        tmp_time = cal_time(t, "23:59")
        fee_record[n] += tmp_time

    sorted_fee = sorted(fee_record.items())

    for _, v in sorted_fee:
        fee = fees[1]
        v -= fees[0]

        if v > 0:
            d, m = divmod(v, fees[2])
            fee += (d+1)*fees[3] if m else d*fees[3]

        answer.append(fee)

    return answer
