import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')
from itertools import combinations

default = set('antic')
N, K = map(int, input().split())
alphabet = {}
for i in range(0, 26):
    alphabet[chr(i+97)] = 1 << i
for d in default:
    alphabet.pop(d)

if K < 5:
    print(0)
else:
    K -= 5
    unlearnt = []
    max_cnt = 0

    for _ in range(N):
        temp = set(input()) - default
        bit1 = 0
        for char in temp:
            bit1 += alphabet.get(char, 0)
        unlearnt.append(bit1)

    for com in combinations(alphabet, K):
        cnt = 0
        bit2 = 0
        for c in com:
            bit2 += alphabet.get(c, 0)

        for ul in unlearnt:
            if bit2 & ul == ul:
                cnt += 1

        if cnt > max_cnt:
            max_cnt = cnt

    print(max_cnt)