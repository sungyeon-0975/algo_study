def solution(n, times):
    answer = 0

    # 최소 최대 시간 초기화
    s, e = 1, max(times) * n

    # 이분 탐색
    while s <= e:
        m = (s+e)//2
        people = 0
        for time in times:
            people += m // time
            if people >= n:
                break

        if people >= n:
            answer = m
            e = m-1

        else:
            s = m+1

    return answer


print(solution(6, [7, 10]))
