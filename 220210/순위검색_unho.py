from itertools import combinations
from pprint import pprint

def solution(infos, query):
    answer = []                 # 정답 리스트
    people = {}                 # 선택한 항목별 점수를 저장할 딕셔너리

    for info in infos:
        info = info.split(' ')  # 입력으로 주어지는 정보들을 사용하기 편리하게 분리

        for k in range(5):                          # 추후에 쿼리를 통해 정보를 찾을때 - 기호가 들어가므로
            for comb in combinations(range(4), k):  # 조합을 이용하여 어느 인덱스에 - 기호를 넣을지 구분
                tmp = []

                for idx in range(4):
                    if idx in comb:                 # 현재 인덱스에 - 기호가 들어가야 하는 경우
                        tmp.append('-')
                    else:                           # 현재 인덱스에 - 기호가 들어가지 않는 경우
                        tmp.append(info[idx])
                
                people[' '.join(tmp)] = sorted(people.get(' '.join(tmp), []) + [int(info[-1])], reverse=True)     # 딕셔너리에 현재 지원자의 점수 추가

    for q in query:
        q = q.split(' ')
        scores = people.get(' '.join(q[:7:2]), {})      # 찾으려는 선택 사항의 키값에 해당하는 점수들을 모두 가져옴
        
        cnt = 0                         # 쿼리문의 점수 이상이 몇개인지 카운트
        for score in scores:
            if score >= int(q[-1]):
                cnt += 1
            else:
                break

        answer.append(cnt)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))