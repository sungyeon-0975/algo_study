written = [[0]*15 for _ in range(5)]

for i in range(5):
    d = list(input())
    for j in range(len(d)):
        written[i][j] = d[j]

for i in range(15):
    for j in range(5):
        if written[j][i] == 0:
            continue
        else:
            print(written[j][i], end='')