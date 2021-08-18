def solution(citations):
    citations.sort(reverse=True)
    
    for i in range(len(citations), -1, -1): # h번 이상이 h개여야 하므로 최대는 len
        cnt = 0
        for idx in range(len(citations)):
            if citations[idx] >= i:
                cnt += 1
            else:
                break
        if len(citations)-cnt <= i <= cnt:
            break
    answer = i
    return answer

print(solution([3, 0, 6, 1, 5]))