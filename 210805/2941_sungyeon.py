if __name__ == "__main__":
    target = input()
    croatian = {'c=','c-','d-','lj','nj','s=','z='}
    c = 0
    idx = 0

    #sol1 : sol2보다 빠름, 메모리는 동일
    while idx < len(target):
        if target[idx:idx+3] == 'dz=':
            idx += 3
        elif target[idx:idx+2] in croatian:
            idx += 2
        else:
            idx += 1
        c += 1

    #sol2
    # while target:
    #     if target[:3] == 'dz=':
    #         target = target[3:]
    #     elif target[:2] in croatian:
    #         target = target[2:]
    #     else:
    #         target = target[1:]
    #     c += 1

    print(c)
