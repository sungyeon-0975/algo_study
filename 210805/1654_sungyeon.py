# 쫌더 제대로 이해필요

import sys
input = sys.stdin.readline

def num_of_lan(length):
    cnt = 0
    for i in lan_list:
        cnt += i//length
    return cnt    


if __name__ == "__main__":
    k,n = map(int,input().split())
    lan_list = [int(input()) for _ in range(k)]
    head = 1
    tail = sum(lan_list)//k
    target = n-1
    while head <= tail:
        mid = (head + tail)//2
        num = num_of_lan(mid)

        if num > target:
            head = mid+1
        elif num == target:
            break
        else:
            tail = mid-1

    while num_of_lan(mid) < n:
        mid -= 1

    print(mid)

        

