def d(n):
    res = n
    while n:
        res += n%10
        n //= 10
    return res

if __name__ == "__main__":
    l = [i for i in range(10000)]
    l = set(map(d,l))
    result = set([i for i in range(10000)]) - l
    for i in sorted(list(result)):
        print(i)
