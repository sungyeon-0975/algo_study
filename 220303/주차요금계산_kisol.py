from math import ceil

def solution(fees, records):
    records = [record.split() for record in records]
    in_out = {key[1]: [] for key in records}
    time = sorted([[key, 0] for key in in_out])  # 차량 번호 오름차순
    answer = [fees[1]] * len(time)

    # 차량 번호별 IN/OUT
    for record in records:
        minutes = int(record[0][:2]) * 60 + int(record[0][3:])
        in_out[record[1]].append(minutes)

    # 누적 주차 시간 구하기(홀수일 경우, 마지막 시간 출차 처리)
    for i in range(len(time)):
        t = time[i]
        minutes = in_out[t[0]]

        for j in range((len(minutes) + 1) // 2):
            out = 1439 if j * 2 == len(minutes) - 1 else minutes[j * 2 + 1]
            t[1] += out - minutes[j * 2]

    # 차량별 요금 계산하기
    for i in range(len(time)):
        if time[i][1] <= fees[0]:
            continue
        answer[i] += ceil((time[i][1] - fees[0]) / fees[2]) * fees[3]

    return answer


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591],
               ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))

# 0000번 차량은 18:59에 입차된 이후, 출차된 내역이 없습니다. 따라서, 23:59에 출차된 것으로 간주합니다.
# 초과한 시간이 단위 시간으로 나누어 떨어지지 않으면, 올림합니다.
# 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return 하도록 solution 함수를 완성해주세요.