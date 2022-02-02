def solution(str1, str2):
    def make_set(word):
        new = list()
        for i in range(1, len(word)):
            if word[i-1].isalpha() and word[i].isalpha():
                temp = word[i-1].lower() + word[i].lower()
                new.append(temp)
        return new

    set1, set2 = make_set(str1), make_set(str2)
    if len(set1) > len(set2):
        inter = len([set1.remove(x) for x in set2 if x in set1])
    else:
        inter = len([set2.remove(x) for x in set1 if x in set2])

    uni = len(set1) + len(set2)

    if not inter and not uni:
        return 65536

    return int(inter/uni*65536)


print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))