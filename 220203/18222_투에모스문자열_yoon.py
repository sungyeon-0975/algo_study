def sol(n):
    if n < 2:
        return n % 2
    if n % 2:
        return 1 - sol(n//2)
    else:
        return sol(n//2)


k = int(input())
print(sol(k-1))