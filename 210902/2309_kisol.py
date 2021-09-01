import sys

# input = sys.stdin.readline
sys.stdin = open('input_2309.txt')
# 80ms

def Find_No_Dwarfs():
    global dwarfs
    for i in range(8):
        for j in range(i + 1, 9):
            if dwarfs[i] + dwarfs[j] == no_dwarfs:
                dwarfs.pop(i)
                dwarfs.pop(j - 1)
                return


dwarfs = sorted([int(input()) for _ in range(9)])
no_dwarfs = sum(dwarfs) - 100
Find_No_Dwarfs()

for i in range(7):
    print(dwarfs[i])
