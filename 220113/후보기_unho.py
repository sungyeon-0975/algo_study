from itertools import combinations                  # 조합 구하기 위한 모듈 임포트

def solution(relation):         
    R = len(relation)                               # DB 행의 개수
    C = len(relation[0])                            # DB 열의 개수
    cols = set()                                    # 유일성과 최소성을 만족하는 후보키 목록

    for i in range(1, C+1):                         # 열이 선택되는 개수
        combs = list(combinations(range(C), i))     # 열이 i개 선택했을때 나오는 모든 조합들

        for comb in combs:                          # 조합 하나씩 확인
            data = set()                            # 각 열의 후보키 값들을 저장할 변수 (집합을 이용해서 겹치는 경우 저장 안되게 사용)

            for e in relation:                      # 각 행별로 데이터 확인을 위한 반복
                tmp = []                            # 후부키의 값들을 담은 임시 리스트 변수
                for i in comb:                      # 조합에서 선택된 열만큼 반복
                    tmp.append(e[i])                # 각 열의 값을 임시변수에 저장
                data.add(tuple(tmp))                # 후보키 값들 저장
            
            if len(data) == R:                      # 모든 후보키 값들이 유일성을 만족하면
                for col in cols:                    # 이전 정답의 후보키 설정 열의 목록 확인
                    if not (set(col) - set(comb)):  # 최소성 확인
                        break
                else:                               # 최소성도 만족하면 답에 추가
                    cols.add(comb)


    return len(cols)


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
print(solution([["a", "1", "aaa", "c", "ng"], ["a", "1", "bbb", "e", "g"], ["c", "1", "aaa", "d", "ng"], ["d", "2", "bbb", "d", "ng"]]))
print(solution([['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]))