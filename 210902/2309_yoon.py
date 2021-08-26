import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')

'''
29200 KB / 80 ms
'''

dwarf = []

for _ in range(9):
    dwarf.append(int(input()))
sub = sum(dwarf) - 100 # 100보다 얼만큼 초과하는지

for idx in range(9):
    leftover = sub - dwarf[idx] # 초과값 - idx 번째 값 (이 두 개 빼줘야됨)
    if leftover in dwarf and leftover != dwarf[idx]:
        dwarf.remove(dwarf[idx])
        dwarf.remove(leftover)
        break

dwarf.sort()
for i in range(7):
    print(dwarf[i])