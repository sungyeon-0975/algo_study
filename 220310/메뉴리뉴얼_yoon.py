from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for num in course:
        temp = []
        for order in orders:
            for comb in combinations(order, num):
                c = ''.join(sorted(comb))
                temp.append(c)
        common = Counter(temp).most_common()
        for menu, cnt in common:
            if cnt > 1 and cnt == common[0][1]:
                answer.append(menu)
    #             if c in temp:
    #                 temp.update({c: temp[c]+1})
    #             else:
    #                 temp.update({c: 1})
    #     if temp:
    #         max_cnt = max(temp.values())
    #         for item in temp.items():
    #             if item[1] == max_cnt and max_cnt != 1:
    #                 answer.append((len(item[0]), item[0]))
    # answer.sort()
    # for i in range(len(answer)):
    #     answer[i] = answer[i][1]
    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))