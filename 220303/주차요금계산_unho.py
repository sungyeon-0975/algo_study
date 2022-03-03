from math import ceil

def solution(fees, records):
    base_time, base_cost, per_time, per_cost = fees             # 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)

    answer = []                 # 정답 리스트
    parking = {}                # 주차장에 차량이 있는지 없는지 여부, 키: 차량 번호, 값: 입차 시간
    times = {}                  # 차량별 주차장 이용 누적시간

    for record in records:
        time, car_number, case = record.split(' ')                      # 시간, 차량 번호, 입출차 여부
        
        time_minutes = int(time[:2]) * 60 + int(time[3:5])              # 문자열 시간을 분으로 변경
                
        if parking.get(car_number, -1) == -1:                           # 입차인 경우 입차 시간 기록
            parking[car_number] = time_minutes
        else:                                                           # 출차인 경우
            times[car_number] = times.get(car_number, 0) + (time_minutes - parking[car_number])     # 누적시간 변수에 추가
            parking.pop(car_number)                                     # 출차되었으면 주차장 변수에서 키값 삭제

    for key in parking.keys():                                          # 출차되지 않은 차량이 있으면
        times[key] = times.get(key, 0) + ((24*60-1) - parking[key])     # 23시 59분에 출차한것으로 기록

    for k in sorted(times.keys()):                                      # 차량 번호 순서대로
        minutes = times[k]                                              # 차량 번호 누적 시간
        cost = base_cost                                                # 기본 요금으로 적용

        if minutes > base_time:                                         # 기본 시간 초과시
            cost += ceil((minutes - base_time) / per_time) * per_cost   # 추가 요금 부과
        
        answer.append(cost)

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))