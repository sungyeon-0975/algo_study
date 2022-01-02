def dfs(pw, idx, cnt):
    if len(pw) == l:
        if len(pw) - cnt >= 2 and cnt:  # 조건 여부
            print(pw)
        return

    for i in range(idx, c):
        if lst[i] in vowel:  # 모음 여부
            dfs(pw+lst[i], i+1, cnt+1)
        else:
            dfs(pw+lst[i], i+1, cnt)


l, c = map(int, input().split())
lst = list(input().split())
vowel = ["a", "e", "i", "o", "u"]
lst.sort()  # 순서대로
dfs("", 0, 0)
