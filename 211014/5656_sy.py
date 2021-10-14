import sys
sys.stdin = open('input.txt')

def select_position(i, removed_cnt):
    global res
    if res < removed_cnt:
        res = removed_cnt
    if i == n:
        return

    for j in range(w):
        k = find_block(j, lengths[j]-1, -1, 1)
        if k > -1:
            changed = remove_blocks(j, k)
            change_blocks(changed, 1)
            select_position(i + 1, removed_cnt + len(changed))
            change_blocks(changed, 0)


def find_block(col, s, e, order):
    c = 0
    for i in range(s, e, -1 if s > e else 1):
        if status[col][i] != 1:
            c += 1
            if c == order:
                return i
    return -1


def remove_blocks(column_idx, row_idx):
    global status
    changed = [(column_idx, row_idx)]
    cnt, ch_idx = 1, 0

    while ch_idx < cnt:
        x, y = changed[ch_idx][0], changed[ch_idx][1]
        ch_idx += 1

        if l[x][y] == 1:
            continue

        # 가로
        order = status[x][:y+1].count(0)
        for j in range(max(x - l[x][y] + 1, 0), min(w, x + l[x][y])):
            if j == x:
                continue
            k = find_block(j, 0, lengths[j], order)
            if k != -1 and (j, k) not in changed:
                cnt += 1
                changed.append((j, k))
        # 세로
        c = 1
        for k in range(y - 1, -1, -1):
            if status[x][k] == 0:
                c += 1
                if (x, k) not in changed:
                    cnt += 1
                    changed.append((x, k))
                if c == l[x][y]:
                    break
        c = 1
        for k in range(y + 1, lengths[x]):
            if status[x][k] == 0:
                c += 1
                if (x, k) not in changed:
                    cnt += 1
                    changed.append((x, k))
                if c == l[x][y]:
                    break
    return changed


def change_blocks(changed_list, val):
    for i, j in changed_list:
        status[i][j] = val


t = int(input())
for idx in range(1, t+1):
    n, w, h = map(int, input().split())
    l = list(map(lambda x: list(filter(lambda x: x != 0, list(x)[::-1])), zip(*[list(map(int, input().split())) for _ in range(h)])))
    lengths = [len(l[i]) for i in range(w)]
    status = [[0] * lengths[i] for i in range(w)]
    res = 0

    select_position(0, 0)
    print('#{} {}'.format(idx, sum(lengths) - res))