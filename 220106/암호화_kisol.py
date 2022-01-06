def solution(sentence, keyword, skips):
    arr = list(sentence)
    idx_sentence = 0
    idx_keyword = 0
    idx_skips = 0

    while idx_sentence < len(arr) + 1 and idx_skips < len(skips):
        flag = True
        for _ in range(skips[idx_skips]):
            if idx_sentence < len(arr) and arr[idx_sentence] == keyword[idx_keyword]:
                idx_sentence += 1
                break
            if idx_sentence >= len(arr):
                flag = False
                break
            idx_sentence += 1

        if flag:
            arr.insert(idx_sentence, keyword[idx_keyword])
            idx_sentence += 1
            idx_skips += 1
            idx_keyword = (idx_keyword + 1) % len(keyword)
        else:
            break

    return ''.join(arr)


print(solution("i love coding", "mask", [0, 0, 3, 2, 3, 4]))
print(solution("i love coding", "mode", [0, 10]))
print(solution("abcde fghi", "axyz", [3, 9, 0, 1]))
print(solution("encrypt this sentence", "something", [0, 1, 3, 2, 9, 2, 0, 3, 0, 2, 4, 1, 3]))