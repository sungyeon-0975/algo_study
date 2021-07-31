if __name__ == "__main__":
    l = [input() for _ in range(5)]
    res = ['']*max(map(len,l))
    for s in l:
        for i in range(len(s)):
            res[i] += s[i]
    print(''.join(res))
