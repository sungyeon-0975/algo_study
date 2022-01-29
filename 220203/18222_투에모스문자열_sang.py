def thue_morse(k):
    cnt = 0
    while k:
        i = len(format(k, "b")) - 1
        k = k - 2**i
        cnt += 1

    return 1 if cnt % 2 else 0


k = int(input())
print(thue_morse(k-1))
