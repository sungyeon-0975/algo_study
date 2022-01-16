import sys
sys.stdin = open('input.txt')

def solution(n, ans):
    if n <= 0:
        print(''.join(ans))
        return
    
    for i in range(M):
        if not selected[i]:                         # 사용하지 않은 단어 리스트
            tmp = ans + [word[i]]                   # 뒤에 사용하지 않은 단어 추가
            if tuple(tmp) not in used:              # 사용한 단어에 포함되지 않으면
                used.add(tuple(tmp))                # 사용한 단어 추가
                selected[i] = 1
                solution(n-1, ans + [word[i]])      # 다음 글자 확인
                selected[i] = 0


N = int(sys.stdin.readline())                           # 단어의 개수

for _ in range(N):
    word = sorted(list(sys.stdin.readline().strip()))   # 입력된 단어를 정렬하여 리스트로 만듦
    used = set()                                      # 중복을 피하기 위한 집합 생성

    M = len(word)               # 단어의 길이
    selected = [0] * M          # 특정 단어 사용 여부 확인을 위한 리스트

    solution(M, [])