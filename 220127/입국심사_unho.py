def solution(n, times):
    times.sort()                # 이분 탐색을 위한 정렬
    answer = 0
    
    l, r = 0, times[-1] * n     # 모든 심사관의 소요되는 최소 시간, 최대 시간
    while l <= r:               
        mid = (l+r) // 2        # 모든 심사관이 mid 분을 이용하여 심사하게 될때
        tmp = 0
        for e in times:
            tmp += mid // e     # 각 심사관들이 mid 분을 이용해 심사했을때 각자 심사 가능한 인원 추가

            if tmp >= n:        # 현재 심사관까지 심사했는데, 모든 인원 심사가 가능한 경우
                answer = mid    # 현재 전체 소요 시간 저장
                r = mid - 1     # 더 짧은 시간으로 가능한지 탐색을 위한 설정
                break
        else:                   # 모든 심사관이 mid 분 동안 모든 인원 심사가 불가능하면
            l = mid + 1         # 더 많은 시간으로 가능한지 탐색

    return answer

print(solution(6, [10, 7]))