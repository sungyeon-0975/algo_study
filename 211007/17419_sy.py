'''
84ms
'''
if __name__ == "__main__":
    n = int(input())
    print(input().count('1'))


    # k = int(input(), 2)
    # res = 0
    # for i in range(n):
    #     if k & (1 << i):
    #         res += 1
    # print(res)

    # res = 0
    # while k:
    #     k -= (k&((~k)+1))
    #     res += 1
    # print(res)

