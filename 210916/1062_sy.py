import sys
input = sys.stdin.readline


def dfs(idx, num):
    global res, len_s, bit_l, bit
    if num == 0 or (num == 0 and idx == len_s):
        cnt = 0
        for i in range(n):
            if bit_l[i] & bit == bit_l[i]:
                cnt += 1
        if cnt > res :
            res = cnt
    elif idx < len_s:
        dfs(idx + 1, num)
        bit += (1 << idx)
        dfs(idx + 1, num - 1)
        bit -= (1 << idx)
        

if __name__ == "__main__":
    n, k = map(int, input().split())
    res = 0
    words = []
    s = set()
    res = 0

    for _ in range(n):
        word = input().strip()
        words.append(word)
        s |= set(word)

    if k < 5:
        print(0)
    else:
        param = [0] * n
        s = list(s - {'a','n','t','i','c'})
        bit_l = [0] * n
        for i in range(len(s)):
            val = s[i]
            for j in range(n):
                if val in words[j]:
                    bit_l[j] += (1 << i)
        len_s = len(s)
        bit = 0
        dfs(0, k-5)

        print(res)
