def solution(sentence, keyword, skips):
    ans = ''
    ls, lk = len(sentence), len(keyword)
    idx = -1
    brk = False

    for i in range(len(skips)):
        word, cnt = keyword[i % lk], skips[i]
        for _ in range(cnt):
            idx += 1

            if idx >= ls:
                brk = True
                break

            ans += sentence[idx]
            if word == sentence[idx]:
                break

        if brk:
            break

        ans += word

    ans += sentence[idx+1:]
    return ans


# "mai lsovke cmodinag"
print(solution("i love coding", "mask", [0, 0, 3, 2, 3, 4]))
print(solution("i love coding", "mode", [0, 10]))  # "mi loove coding"
print(solution("abcde fghi",   "axyz",  [3, 9, 0, 1]))  # "aabcde fghixy"
print(solution("encrypt this sentence", "something", [
      0, 1, 3, 2, 9, 2, 0, 3, 0, 2, 4, 1, 3]))  # "seoncrmypett thihisng ssenteonmcee"
