def dfs(begin, target, words, visited, ans):    # 현재 단어 / 목표 단어 / 단어들 목록 / 방문처리 변수 / 현재까지 소요된 변환 횟수
    global answer

    if begin == target:                         # 현재 단어가 찾으려는 단어일때
        answer = ans                            # 변환된 횟수를 저장
        return
    elif answer < ans:                          # 현재까지 변환된 횟수가 최소로 변환된 횟수보다 클때, 현재 경우 종료
        return

    for i in range(len(words)):                 # 단어들 집합에서 각 단어들 확인
        if not visited[i]:                      # 아직 변환된 단어가 아니면 확인
            need_change = 0                     # 바꿔야 할 글자수 개수 체크하는 변수
            
            for k in range(len(begin)):         # 각 단어의 자릿수들 비교하여 알파벳이 일치하지 않으면
                if begin[k] != words[i][k]:     # 바꿔야 할 글자수 체크하는 변수 1 증가
                    need_change += 1
            
            if need_change == 1:                                # 바꿔야 할 글자수가 1개이면 실행
                visited[i] = 1                                  # 현재 단어로 변경되었으므로 방문 처리
                dfs(words[i], target, words, visited, ans+1)    # 이어서 DFS 탐색
                visited[i] = 0                                  # 방문 취소 처리


def solution(begin, target, words):
    global answer

    answer = 1e10                           # 최소 변환 횟수를 구해야하므로 초기값은 임의의 큰 수
    visited = [0] * len(words)              # 각 단어들로 변환했는지 여부 체크를 위한 방문 변수ㄴ

    dfs(begin, target, words, visited, 0)   # dfs 탐색

    if answer == 1e10:                      # 변환 불가능한 경우 0 출력
        return 0
    return answer


print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))