def solution(str1, str2):
    one, two = {}, {}       # 문자열들을 2글자씩 자른 갯수를 카운트하는 딕셔너리 변수
    intersection = 0        # 교집합의 개수
    union = 0               # 합집합의 개수

    for i in range(1, len(str1)):       # 첫번째 문자열의 두글자가 문자열로만 이루어져 있으면
        if str1[i-1:i+1].isalpha():     # 딕셔너리에 없는 문자이면 키를 새로 생성하고, 1씩 증가
            one[str1[i-1:i+1].lower()] = one.get(str1[i-1:i+1].lower(), 0) + 1
        
    for i in range(1, len(str2)):
        if str2[i-1:i+1].isalpha():
            two[str2[i-1:i+1].lower()] = two.get(str2[i-1:i+1].lower(), 0) + 1

    for k in set(list(one.keys()) + list(two.keys())):          # 첫번째 문자열과 두번쨰 문자열의 키값들 서로 교집합 합집합 확인
        intersection += min(one.get(k, 0), two.get(k, 0))       # 교집합의 개수 카운트
        union += max(one.get(k, 0), two.get(k, 0))              # 합집합의 개수 카운트


    if not union:           # 합집합이 없으면 자카드 유사도는 1이 된다
        return 65536
    return int(intersection / union * 65536)

print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))