ans = set()


def check():
    for x, y, t in ans:
        if not t:
            if y == 0 or (x, y-1, 0) in ans or (x, y, 1) in ans or (x-1, y, 1) in ans:
                continue
            else:
                return False

        else:
            if (x, y-1, 0) in ans or (x+1, y-1, 0) in ans or (((x-1, y, 1) in ans) and ((x+1, y, 1) in ans)):
                continue
            else:
                return False

    return True


def solution(n, build_frame):
    answer = []

    for build in build_frame:
        x, y, t, s = build
        frame = (x, y, t)

        if s:
            ans.add(frame)
            if not check():
                ans.remove(frame)

        else:
            ans.remove(frame)
            if not check():
                ans.add(frame)

    answer = sorted(ans)

    return answer
