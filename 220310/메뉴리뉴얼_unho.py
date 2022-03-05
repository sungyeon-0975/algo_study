from itertools import combinations

def solution(orders, course):
    answer = []                                         # 정답 리스트
    li_orders = []                                      # 손님들이 주문한 메뉴들이 문자열로 들어와서, 메뉴 하나씩 나누어 하나의 리스트에 담음
    combs = set()                                       # 나올 수 있는 메뉴 조합들
    max_cnt = [0] * (max(course)+1)                     # 메뉴 개수별로 나올수 있는 조합들 중 제일 많이 주문된것을 찾아야하므로
    ans = [[] for _ in range(max(course)+1)]            # 메뉴 개수별 조합들

    for order in orders:                                # 손님들 주문 내역을 리스트로 변환
        li_orders.append(set(order))
    
    for order in li_orders:                             # 손님들 주문별
        for n in course:                                # 조합을 만들어야하는 메뉴 개수
            for comb in combinations(order, n):         # 조합 생성
                comb = tuple(sorted(comb))
                combs.add(comb)                         # 손님이 주문할 수 있는 전체 조합에 추가

    for comb in combs:                                  # 주문 가능한 전체 조합들 반복
        cnt = 0                                         # 이 조합으로 주문한 손님의 수
        n = len(comb)                                   # 조합의 메뉴 개수
        for order in li_orders:
            if n <= len(order) and not set(comb).difference(order):     # 해당 손님이 이 조합으로 주문한적이 있으면
                cnt += 1                                                # 주문한 손님 수 증가
        
        if cnt >= 2 and max_cnt[n] <= cnt:              # 2명 이상이 주문하였고, 제일 많이 주문한 메뉴일때
            if max_cnt[n] < cnt:                        # 최대 주문 횟수 갱신시, 이전 주문 조합 제거
                ans[n].clear()
            max_cnt[n] = cnt                            
            ans[n].append(''.join(sorted(comb)))        # 최대 주문 횟수의 조합 추가

    for a in ans:           # 모든 조합들 정답 리스트에 추가
        answer.extend(a)

    answer.sort()

    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))