'''
실행시간 : 664ms
'''
import math

if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split()))
    b,c = map(int, input().split())

    print(sum(map(lambda x : math.ceil((x-b)/c)+1  if x >= b else 1, l)))

