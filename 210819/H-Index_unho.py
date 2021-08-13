'''
리스트에 h보다 큰수를 카운트 하면 시간 복잡도 증가
정렬하면 특정 인덱스 이전 또는 이후에는 크거나 작은수가 몇개가 있는지 보장됨
'''


def solution(citations):
    citations.sort()                                    # 시간복잡도 관리 위한 정렬  

    h = 0                                               # 리스트 인덱스 에러 방지 위한 조건 및
    while h <= len(citations) and citations[-h] >= h:   # 오름차순이므로 뒤에서 h 번째 값이 h 보다 크거나 같으면 H-index 조건 충족됨
        h += 1
    
    return h-1

print(solution([3,0,6,1,5]))
print(solution([1,0,2,2,3,3]))
print(solution([0,0,0,0,0]))
print(solution([1]))