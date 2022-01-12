from itertools import combinations

def solution(relation):

    col = len(relation[0])
    row = len(relation)
    keys = set()

    for i in range(1, col+1):
        cases = combinations(range(col), i)
        # print(list(cases))
        for case in cases:                      # 열 번호 리스트
            check = set()
            for j in relation:
                temp = []
                for c in case:
                    temp.append(j[c])
                check.add(tuple(temp))
            if len(check) == row:
                # 아오



    return answer


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))