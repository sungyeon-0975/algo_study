'''
72ms
'''

if __name__ == "__main__":
    length = int(input())
    res = 0
    for i in range(7):
        if length & (1 << i):
            res += 1
    print(res)
