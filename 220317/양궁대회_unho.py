def solution(n, info):
    answer = []                 # 점수 받는 정답 리스트
    max_difference = 0          # 가장 많이 차이 나는 점수차

    def sol(idx, remain, apeach, ryan, ans):                            # 인덱스, 남은 화살 수, 어피치 점수, 라이언 점수, 점수별 라이언이 쏜 화살 수
        nonlocal answer, max_difference

        if idx > 10 and remain >= 0:                                    # 모두 반복했고, 화살이 남거나 다 쐈을때
            if max_difference <= ryan - apeach:                         # 점수차 최대 이상일때
                if max_difference < ryan - apeach:                      # 점수차 새로 갱신시 기존에 기록한 정답 리스트 초기화
                    answer.clear()       
                if remain:                                              # 화살이 모두 남아있을때 모두 0점에 쏜것으로 처리
                    ans[-1] += remain                            
                max_difference = ryan - apeach                          # 점수차 새로 기록
                answer.append(ans)                                      # 정답에 추가
            return
        elif remain < 0:                                                # 화살 쏜 횟수 초과시 그냥 종료
            return

        sol(idx+1, remain-info[idx]-1, apeach, ryan+(10-idx), ans+[info[idx]+1])        # 이번 점수 이길때
        sol(idx+1, remain, apeach+(10-idx) if info[idx] else apeach, ryan, ans+[0])     # 이번 점수 질때

    sol(0, n, 0, 0, [])                                                 # 탐색 시작

    answer = sorted(answer, key=lambda x: list(x[k] for k in range(10, -1, -1)))        # 가장 마지막에 쏜 화살이 적은 순으로 정렬

    return answer[-1] if max_difference else [-1]

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))