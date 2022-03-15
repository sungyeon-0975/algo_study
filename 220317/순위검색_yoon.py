# def solution(info, query):
#     answer = []
#     applicant = []
#     for i in range(len(info)):
#         app = list(map(str, info[i].split()))
#         applicant.append(app)
#     for j in range(len(query)):
#         q = list(map(str, query[j].split(' and '))) + [0]
#         q[3], q[4] = q[3].split()
#         temp = 0
#         for k in range(len(applicant)):
#             flag = True
#             for l in range(4):
#                 if applicant[k][l] == q[l] or q[l] == '-':
#                     continue
#                 else:
#                     flag = False
#                     break
#             if int(applicant[k][4]) >= int(q[4]) and flag:
#                 temp += 1
#         answer.append(temp)
#     return answer
#
# print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

from collections import defaultdict
from itertools import product
from bisect import bisect_left

def solution(info, query):
    answer = []
    information = defaultdict(list)
    conditions = list(product((0, 1), repeat=4))

    for app in info:
        app = app.split()
        for con in conditions:
            key = ''.join([app[k] if con[k] else '-' for k in range(4)])
            information[key].append(int(app[4]))

    for i in information.keys():
        information[i].sort()

    for q in query:
        lang, _, pos, _, year, _, food, score = q.split()
        key = lang + pos + year + food
        left = bisect_left(information[key], int(score))
        answer.append(len(information[key]) - left)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))