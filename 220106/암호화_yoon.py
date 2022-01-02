def solution(sentence, keyword, skips):
    result = ''
    for i in range(len(skips)):
        skip = skips[i]
        key = keyword[i % len(keyword)]
        now, sentence = sentence[:skip], sentence[skip:]
        if key in now:
            idx = now.index(key)
            now1, now2 = now[:idx+1], now[idx+1:]
            result += (now1 + key)
            sentence = now2 + sentence
        else:
            result += (now + key)
        if len(sentence) == 0 and i < len(skips) - 1:
            if skips[i+1] == 0:
                continue
            else:
                break
    result += sentence
    return result


print(solution("i love coding", "mask", [0, 0, 3, 2, 3, 4]))
print(solution("i love coding", "mode", [0, 10]))
print(solution("abcde fghi", "axyz", [3, 9, 0, 1]))
print(solution("encrypt this sentence", "something", [0, 1, 3, 2, 9, 2, 0, 3, 0, 2, 4, 1, 3]))