import sys
sys.stdin = open('input.txt')


word1 = input()
word2 = input()

N = len(word1)      
M = len(word2)

if M > N:                           # 두번째 문자가 더 길면 스왑
    word1, word2 = word2, word1     # word1, N 이 더 길게끔
    M, N = N, M

word1_index = {}    # 각 문자의 알파벳이 위치한 인덱스를 담는 딕셔너리
word2_index = {}

for i in range(N):                       # 각 알파벳이 어디있는지 위치 저장
    word1_index[word1[i]] = word1_index.get(word1[i], []) + [i]
    if i < M:
        word2_index[word2[i]] = word2_index.get(word2[i], []) + [i]

# print(f'word1_index : {word1_index}')
# print(f'word2_index : {word2_index}')

idx = 0
while idx < N:
    idx += 1