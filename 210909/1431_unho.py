'''
use quicksort

Memory - 29200 KB
Time - 96 ms
'''

import sys
sys.stdin = open('input_1431.txt')



def serial_sum(s):              # 각 자릿수의 합을 반환하는 함수
    result = 0

    for c in s:
        if c.isdigit():
            result += int(c)
    return result

def quicksort(arr):             # 퀵정렬
    # Base Case
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    more = []                       # 작은거
    less = []                       # 큰거
    equal = []                      # 같은거
    p_len = len(pivot)              # 피벗 길이
    p_sum = serial_sum(pivot)       # 피벗 숫자들 합


    for e in arr:
        tmp_len = len(e)            # 비교 문자 길이
        tmp_sum = serial_sum(e)     # 비교 문자 숫자들 합

        if pivot == e:
            equal.append(e)

        elif p_len < tmp_len:       # first
            more.append(e)
        elif p_len > tmp_len:
            less.append(e)
        
        elif p_sum < tmp_sum:       # second
            more.append(e)
        elif p_sum > tmp_sum:
            less.append(e)
        
        else:                       # third
            tmp_li = sorted([pivot, e])
            if tmp_li[0] == pivot:
                more.append(e)
            else:
                less.append(e)

    return quicksort(less) + equal + quicksort(more)


test_case = int(input())

for _ in range(test_case):
    N = int(input())
    guitar = [input() for _ in range(N)]

    sorted_guitar = quicksort(guitar)

    for idx in range(N):
        print(sorted_guitar[idx])