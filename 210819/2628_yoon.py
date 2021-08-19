import sys
input = sys.stdin.readline

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