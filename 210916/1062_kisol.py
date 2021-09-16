import sys
from itertools import combinations

# KB / ms 비트마스킹으로 풀어보기
# input = sys.stdin.readline
sys.stdin = open('input_1062.txt')


# [비트 마스킹]

def Find_Comb(idx, chars_bit):
    global max_cnt

    if idx == K:
        cnt_words = 0
        for bit in words_bit:
            if i | bit == i:  # 각 word 안의 글자와 차이나지 않으면
                cnt_words += 1
        if cnt_words > max_cnt:
            max_cnt = cnt_words
        return

    for i in range((1 << K) - 1, 1 << len(words_chars)):  # 모든 조합의 가짓수 확인
        cnt = 0  # 조합 내 요소의 개수 count
        for j in range(len(words_chars)):
            if i & (1 << j):
                cnt += 1  # 조합 내 요소의 개수 cnt

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())  # N: 단어 개수, K: 글자 개수
    K -= 5

    if K < 0:  # 최소 단어 요건 충족 못함 ('anta', 'tica')
        words = [input() for _ in range(N)]
        print(0)
    else:
        required_chars = {'a', 'n', 't', 'i', 'c'}
        input_words = [set(input()).difference(required_chars) for _ in range(N)]
        words = []
        max_cnt = 0
        words_chars = set()

        for word in input_words:
            if len(word) <= K:
                words_chars = words_chars.union(word)
                words.append(list(word))

        words_chars = list(words_chars)
        words_chars_bit = (1 << len(words_chars)) - 1
        words_bit = [0 for _ in range(len(words))]

        for i in range(len(words)):
            for char in words[i]:
                words_bit[i] = words_bit[i] | (1 << words_chars.index(char))

        print(max_cnt)


# [itertools 활용]
# T = int(input())
# 
# for _ in range(T):
#     N, K = map(int, input().split())  # N: 단어 개수, K: 글자 개수
#     K -= 5
# 
#     if K < 0:  # 최소 단어 요건 충족 못함 ('anta', 'tica')
#         words = [input() for _ in range(N)]
#         print(0)
#     else:
#         required_chars = {'a', 'n', 't', 'i', 'c'}
#         input_words = [set(input()).difference(required_chars) for _ in range(N)]
#         words = []
#         pick_chars = [0] * K
#         max_cnt = 0
#         words_chars = set()
# 
#         for word in input_words:
#             if len(word) <= K:
#                 words_chars = words_chars.union(word)
#                 words.append(word)
#         words_chars = list(words_chars)
# 
#         combs = combinations(words_chars, K)
#         for comb in combs:
#             cnt = 0
#             for i in range(len(words)):
#                 if not words[i].difference(comb):  # char 안의 단어와 차이나는게 0개라면
#                     cnt += 1
#             if cnt > max_cnt:
#                 max_cnt = cnt
# 
#         print(max_cnt)


# [조합 구현]
# def Find_Comb(idx, start):
#     global pick_chars, max_cnt
#     if max_cnt == N:
#         return
#
#     if idx == K:
#         cnt = 0
#         for i in range(len(words)):
#             if not words[i].difference(pick_chars):  # char 안의 단어와 차이나는게 0개라면
#                 cnt += 1
#         if cnt > max_cnt:
#             max_cnt = cnt
#         return
#
#     for i in range(start, len(words_chars)):
#         if check[i] == 0:
#             pick_chars[idx] = words_chars[i]
#             check[i] = 1
#             Find_Comb(idx + 1, i + 1)
#             pick_chars[idx] = 0
#             check[i] = 0
#
#
# T = int(input())
#
# for _ in range(T):
#     N, K = map(int, input().split())  # N: 단어 개수, K: 글자 개수
#     K -= 5
#
#     if K < 0:  # 최소 단어 요건 충족 못함 ('anta', 'tica')
#         words = [input() for _ in range(N)]
#         print(0)
#     else:
#         required_chars = {'a', 'n', 't', 'i', 'c'}
#         input_words = [set(input()).difference(required_chars) for _ in range(N)]
#         words = []
#         pick_chars = [0] * K
#         max_cnt = 0
#         words_chars = set()
#
#         for word in input_words:
#             if len(word) <= K:
#                 words_chars = words_chars.union(word)
#                 words.append(word)
#         words_chars = list(words_chars)
#         check = [0] * len(words_chars)
#
#         Find_Comb(0, 0)
#         print(max_cnt)
