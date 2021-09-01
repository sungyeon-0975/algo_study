if __name__ == "__main__":
    l = sorted([int(input()) for _ in range(9)])
    total = sum(l)
    find = False
    for i in range(9):
        for j in range(9):
            if total - l[i] - l[j] == 100:
                find = True
                break
            # elif total - l[i] - l[j] < 100:
            #     break
        if find:
            break

    for k in range(9):
        if k not in [i,j]:
            print(l[k])
