from bisect import bisect_left

def solution(infos, query):
    answer = []                 # 정답 리스트
    people = {}                 # 선택한 항목별 점수를 저장할 딕셔너리

    def make_dict():                                                        # 쿼리로 나올 수 있는 모든 경우를 키로 만들어서 딕셔너리 생성
        for a in ('cpp', 'java', 'python', '-'):
            for b in ('backend', 'frontend', '-'):
                for c in ('junior', 'senior', '-'):
                    for d in ('chicken', 'pizza', '-'):
                        people[f'{a} {b} {c} {d}'] = []                     # 초기 비어있는 배열 생성

    def saved_infos(info: str):                                             # 정보들 해당할 수 있는 경우의 배열에 입력
        info = info.split(' ')                                              # 입력으로 주어지는 정보들을 사용하기 편리하게 분리
        
        for a in (info[0], '-'):                    
            for b in (info[1], '-'):
                for c in (info[2], '-'):
                    for d in (info[3], '-'):
                        people[f'{a} {b} {c} {d}'].append(int(info[4]))     # 점수 추가

    def dict_order():                                                       # 쿼리문에서 이진 탐색을 위한 점수 배열 정렬
        for k in people.keys():
            people[k] = sorted(people[k])

    def find_answer(q: str):                                                # 쿼리문 반복하여 정답 찾는 함수
        q = q.split(' ')                                                    # 찾으려는 정보 문자열 배열로 정리
        scores = people.get(' '.join(q[:7:2]), [])                          # 찾으려는 선택 사항의 키값에 해당하는 점수들을 모두 가져옴
        cnt = len(scores) - bisect_left(scores, int(q[-1]))                 # 이분탐색 통해 개수 찾기
        answer.append(cnt)                                                  # 정답 리스트에 추가

    make_dict()                 # 초기 딕셔너리 생성

    for info in infos:          # 정보들 추가
        saved_infos(info)

    dict_order()                # 딕셔너리 값들 정렬

    for q in query:             # 정답 찾기
        find_answer(q)

    return answer

print(solution([
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"
    ], [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150"
    ]))