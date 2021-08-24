def solution(new_id):
    # 1단계
    # new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    
    new_id = new_id.lower() # lower는 그 값을 변경하는 것이 아닌 변경한 것을 반환값으로 돌려줌 
    
    # 2단계
    # new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.

    for i in new_id:
        if not (('a'<= i <= 'z') or ('0' <= i <= '9') or\
           (i == '-') or (i == '_') or (i == '.')):
            new_id = new_id.replace(i, '')  # replace는 그 값을 변경하는 것이 아닌 변경한 것을 반환값으로 돌려줌
    
    # 3단계
    # new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.

    flag = 1
    while flag: # flag가 0일 때 까지 진행
        if new_id.count('..'):  # new_id에 ..이 존재하면
            flag = 1            # flag에 1을 넣어줌
        else:                   # ..이 없으면
            flag = 0            # flag에 0을 넣어줌
        new_id = new_id.replace('..', '.')  # new_id의 ..을 .으로 교체함
        
    # 4단계
    # new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.

        new_id = new_id.lstrip('.') # 왼쪽에서 . 제거
        new_id = new_id.rstrip('.') # 오른쪽에서 . 제거

    # 5단계
    # new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.

    if not new_id: # 빈 문자열이면
        new_id = 'a' # a 넣어줌
        
    # 6단계
    # new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     #만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.

    if len(new_id) >= 16:     # new_id의 길이가 16이상이면
        new_id = new_id[:15]  # 15글자까지 자름
        
    new_id = new_id.rstrip('.') # 오른쪽에서 . 제거
    
    # 7단계
    # new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    
    while len(new_id) <= 2:     # 문자열 길이가 2 이하일 동안
        new_id += new_id[-1]    # new_id에 new_id의 마지막 글자를 추가함
    
    return new_id