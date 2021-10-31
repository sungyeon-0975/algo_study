import sys
input = sys.stdin.readline
from itertools import permutations

def nogada(num_list, dungeons, result, k):
    num_list = list(permutations(num_list))     # 모든 경우의 수
    for idx_list in num_list:                   # 경우의 수 순회
        piro = k - dungeons[idx_list[0]][1]     # 첫 piro에 k - 첫 던전 소모 피로도 뺀 값을 넣어줌
        temp = 1    # 던전 탐험 횟수
        for idx in range(len(idx_list) - 1):    # idx_list 마지막 전 까지만 확인
            if piro >= dungeons[idx_list[idx + 1]][0]:      # piro가 그 다음 던전 최소 필요 피로도 이상이면
                temp += 1   # 던전 탐험 횟수 + 1
                piro = piro - dungeons[idx_list[idx + 1]][1]    # piro에 그 다음 경우의 소모 피로도 뺀 값을 넣음
            if result < temp:   # result가 temp보다 작으면
                result = temp   # result를 temp로 변환
    return result

def solution(k, dungeons):
    num_list = [x for x in range(len(dungeons))]    # num_list 에 0 ~ 던전 갯수를 넣어줌
    result = nogada(num_list, dungeons, 0, k)       # result에 nogada 함수 리턴값을 넣어줌
    return result

print(solution(80, [[80,20],[50,40],[30,10]]))