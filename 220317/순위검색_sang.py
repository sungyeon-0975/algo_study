from bisect import bisect_left
from collections import defaultdict
from itertools import combinations


def solution(info, query):
    answer = []
    db = defaultdict(list)

    for user in info:                
        user_info = user.split()
        cond, score  = user_info[:-1], int(user_info[-1])

        for n in range(5):           
            comb = list(combinations(range(4), n))
            for c in comb:
                tmp = cond.copy()
                for i in c:         
                    tmp[i] = '-'

                db_key = ''.join(tmp)
                db[db_key].append(score)

    for value in db.values():          
        value.sort()
 
    for q in query:                      
        qry = [i for i in q.split() if i != 'and']
        cond, score = ''.join(qry[:-1]), int(qry[-1])
            
        data = db[cond]
        answer.append(len(data)-bisect_left(data, score))

    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
