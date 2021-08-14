import sys
input = sys.stdin.readline

# 놀러와서 풀었기 때문에 생각나는대로 그냥 빨리 푸느라 코드가 아주 길고 더러움
# 나중에 다시 풀어볼게요

horizontal, vertical = map(int, input().split())
lines = int(input())
h_cut = [0, vertical]
v_cut = [0, horizontal]
for i in range(lines):
    line = list(map(int, input().split()))
    # 0이 가로 1이 세로
    if line[0] == 0:
        h_cut.append(line[1])
    else:
        v_cut.append(line[1])
h_cut.sort()
v_cut.sort()
h_gap, v_gap = 0, 0
for h in range(len(h_cut)-1):
    if h_cut[h+1] - h_cut[h] > h_gap:
        h_gap = h_cut[h+1] - h_cut[h]
for v in range(len(v_cut)-1):
    if v_cut[v+1] - v_cut[v] > v_gap:
        v_gap = v_cut[v+1] - v_cut[v]

area = h_gap * v_gap
print(area)