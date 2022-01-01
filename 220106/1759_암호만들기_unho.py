import sys
sys.stdin = open('input.txt')


def solution(n, idx, ans):                          # 현재 알파벳 선택한 개수, 시작할 인덱스 번호, 지금까지 만든 단어
    global vowel_cnt, consonant_cnt

    if n >= L:                                      # 원하는 길이 만들어졌으면 확인
        if vowel_cnt and consonant_cnt >= 2:        # 모음이 1개 이상, 자음이 2개 이상으로 만들어 진 경우
            answer.append(''.join(ans))             # 정답 리스트에 추가
        return
    

    for c in range(idx, C):                         # 이전에 끝난 인덱스 이후부터 시작
        if not selected[c]:
            selected[c] = 1

            if character_list[c] in vowel:          # 모음이면 모음 개수 카운트 증가, 자음이면 자음 개수 카운트 증가
                vowel_cnt += 1
            else:                                  
                consonant_cnt += 1

            ans.append(character_list[c])           # 알파벳 추가
            solution(n+1, c+1, ans)                 # 다음 알파벳 찾으러 재귀
            ans.pop()                               # 알파벳 제거

            if character_list[c] in vowel:          # 모음, 자음 종류에 맞게 개수 카운트 감소
                vowel_cnt -= 1
            else:
                consonant_cnt -= 1

            selected[c] = 0


L, C = map(int, sys.stdin.readline().split())           # 문자의 길이, 문자들의 총 개수
character_list = sorted(sys.stdin.readline().split())   # 문자들 리스트 (사전순으로 단어를 만들어야하므로 사전순 정렬)
vowel = set(['a', 'e', 'i', 'o', 'u'])                  # 모음 리스트
selected = [0] * C                                      # 특정 알파벳 사용 여부

vowel_cnt = 0               # 모음 개수 카운트 변수
consonant_cnt = 0           # 자음 개수 카운트 변수
answer = []                 # 정답 리스트

solution(0, 0, [])          # 완전 탐색

print('\n'.join(answer))    # 출력