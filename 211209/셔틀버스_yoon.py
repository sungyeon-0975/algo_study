def solution(n, t, m, timetable):
    timetable = [int(time[:2]) * 60 + int(time[3:5]) for time in timetable]
    timetable.sort()
    last = 60 * 9 + (n-1) * t

    for i in range(n):
        if len(timetable) < m:
            return '%02d:%02d' % (last // 60, last % 60)
        elif i == n-1:
            if timetable[0] <= last:
                last = timetable[m-1] - 1
            return '%02d:%02d' % (last // 60, last % 60)
        for j in range(m-1, -1, -1):
            bus = 60 * 9 + i * t
            if timetable[j] <= bus:
                del timetable[j]

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))