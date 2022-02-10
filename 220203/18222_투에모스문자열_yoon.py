def sol(n):
    print(n)
    if n < 2:
        return n % 2
    if n % 2:
        return 1 - sol(n//2)
    else:
        return sol(n//2)


k = int(input())
print(sol(k-1))


# 0
# 01
# 0110
# 01101001
# 0은 다음 턴에서 01이 되고 1은 10이 됨
# 그래서 짝수번일때는 그냥 그대로 0-0 1-1인데 홀수번일때는 이전 숫자의 보수로 return