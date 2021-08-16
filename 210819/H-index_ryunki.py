citations = [3, 0, 6, 1, 5]


# 핵심은 리스트를 정렬시키고 거꾸로 인덱스를 매긴후에 매긴 인덱스가 리스트보다 작거나 같아지는 지점이라고 생각했지만 최댓값을 찾기 위해서는 오히려 반대로
# 리스트의 최소값부터 시작해서 리스트의 값이 거꾸로 매긴 인덱스보다 크거나 같아지는 값을 찾아야만 했다.
def solution(citations):
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations)-i:
            return len(citations)-i
    return 0

#
# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer



print(solution(citations))
