"""
단순 그리디 X -> 0번 기준으로 정렬 or 1번 기준으로 정렬 할 경우 예외 발생
    -> 완전 탐색

시간초과 -> 가지치기??
"""


def permu(arr, idx, remain_fatigue, ans):       # 배열 / 인덱스 / 남은 피로도 / 방문한 던전 개수
    global answer

    if idx >= len(arr):     # 던전을 방문할수있는지 모두 확인하면
        if ans > answer:    # 현재 방문한 던전의 개수가 최대인지 확인
            answer = ans
        return
    elif len(arr) - idx + ans <= answer:        # 앞으로 확인할 수 있는 던전의 개수 + 현재 방문한 던전 개수 < 최대 방문 횟수
        return                                  # 앞으로 던전을 더 확인해봤자 최댓값이 나올 수 없음

    for i in range(len(arr)):
        if not visited[i] and remain_fatigue >= arr[i][0]:          # 아직 방문하지 않았고, 방문할 수 있는 던전일때
            visited[i] = 1
            permu(arr, idx+1, remain_fatigue-arr[i][1], ans+1)      # 현재 던전 방문하여 피로도 감소하고 재귀호출
            visited[i] = 0                  
            permu(arr, idx+1, remain_fatigue, ans)                  # 현재 던전 방문할 수 있으나, 방문하지 않고 다른 던전 방문 위해 재귀 호출


def solution(k, dungeons):
    global visited

    visited = [0] * (len(dungeons))         # 해당 던전을 방문했는지 저장하는 리스트

    permu(dungeons, 0, k, 0)

    return answer


answer = 0
visited = []


print(solution(150, [[10,10],[10,10],[80,20],[50,40],[30,10],[10,10],[10,10],[10,10],[10,10],[10,10]]))