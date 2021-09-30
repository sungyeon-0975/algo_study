import sys
sys.stdin=open('input_2112.txt')

for test in range(1,1+int(input())):
    D,W,K = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(D)]
