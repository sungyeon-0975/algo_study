'''
396ms/352ms/348ms
- input 정의 해주는거랑 그냥 바로 sys.stdin.readline쓰는거랑 4ms차이(input 정의한게 348ms)
- 그때그때 출ㄹ력하는거 말고 한꺼번에 출력하는거 (332ms)
'''

from functools import reduce
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    res = []
    for _ in range(n):
        # print(reduce(lambda x,y: x|y, map(int, input().split())), end=' ')
        res.append(reduce(lambda x,y: x|y, map(int, input().split())))
    print(*res)


