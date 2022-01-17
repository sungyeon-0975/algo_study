def solution(s):
    answer = []
    
    li = sorted(s[2:-2].split('},{'), key=lambda x: len(x)) # 양 끝의 중괄호 삭제,  '},{' 기준으로 원소들 구분 후 원소의 개수순으로 정렬
    
    for e in li:                                            # 각 원소들 반복
        num = set(e.split(',')) - set(answer)               # 정답에 있는 현재 길이의 원소와 정답 원소들의 차집합을 구함
        answer.append(num.pop())                            # 아직 정답에 추가 안된 원소를 추출 및 정답에 추가
        
    answer = list(map(lambda x: int(x), answer))            # 정답 각 원소들을 정수형으로 변경
    
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))