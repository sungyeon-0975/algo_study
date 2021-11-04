from itertools import permutations

def solution(k,dungeons):
    answer = 0

    myper = permutations([x for x in range(len(dungeons))])
    # print(list(myper))
    for i in myper:
        K, ans = k,0
        for j in i:
            tempmin , cnt = dungeons[j]
            if K >= tempmin:
                K-=cnt
                ans+=1
        answer = max(answer,ans)
    return answer

print(solution(80,[[80,20],[50,40],[30,10]]))