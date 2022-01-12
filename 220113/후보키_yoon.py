from itertools import combinations

def solution(relation):
    col = len(relation[0])
    row = len(relation)
    keys = []
    for i in range(1, col+1):
        cases = combinations(range(col), i)
        # print(list(cases))
        for case in cases:                      # 열 번호 comb
            check = set()
            for j in relation:                  # 주어진 리스트의 각 행마다
                temp = []
                for c in case:                  # comb에 따라 결과값 추가
                    temp.append(j[c])
                check.add(tuple(temp))          # 개수 확인할 set에 전체 결과값 넣어줌
            if len(check) == row:               # check의 길이가 열 개수만큼이면 유일한 값
                for k in keys:
                    if not set(k) - set(case):  # keys에 이미 최소성을 만족하는 후보키가 있다면 break
                        break
                else:
                    keys.append(tuple(case))    # 아니면 후보키로 추가
    return len(keys)


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))