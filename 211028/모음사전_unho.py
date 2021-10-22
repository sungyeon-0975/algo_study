def product(idx, n):                # 데카르트곱?
    if idx >= n:                    # 인덱스가 글자수 보다 크거나 같아지면
        li.append(''.join(arr))     # 구해진 리스트를 문자열로 이어 붙여서 리스트에 추가해줌
        return
    
    for i in range(5):              # 문자가 aeiou 로 5개이므로 그 중 하나가 선택되어야 하므로 5번 반복
        arr[idx] = char[i]          # 현재 위치의 글자를 aeiou 를 차례대로 넣어줌
        product(idx+1, n)           # 재귀 호출, 글자 위치 + 1


def solution(word):
    return li.index(word) + 1       # 일치하는 문자열이 몇번째 인덱스인지 찾아서 + 1


char = ['A', 'E', 'I', 'O', 'U']
li = []                                 # 나올 수 있는 경우의 문자들을 하나씩 저장할 리스트 변수

for i in range(1, 6):                   # 최소 1글자, 최대 5글자이므로
    arr = [''] * i                      # 현재 글자수만큼 배열의 리스트를 만들어줌
    product(0, i)                       # 시작 인덱스, 글자수
li.sort()                               # 모든 글자들을 사전순으로 정렬


print(solution('AAAAE'))
print(solution('AAAE'))
print(solution('I'))
print(solution('EIO'))
print(solution('UUUUU'))