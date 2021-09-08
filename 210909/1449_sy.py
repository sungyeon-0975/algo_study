'''
실행시간 : 76ms
'''
if __name__ == "__main__":
    n,l = map(int, input().split())
    point = sorted(list(map(int, input().split())))
    covered, res = 0, 0

    for i in point:
        if i + 0.5 > covered:
            res += 1
            covered = i - 0.5 + l
    print(res)
        

