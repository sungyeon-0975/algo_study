import sys
# input = sys.stdin.readline
sys.stdin = open('input_17419.txt')

'''
31156KB / 84ms
'''

# (~K) + 1 = -K
# K - (K & -k) : 맨 뒤의 1만 제거
N = int(input())
K = str(input())
print(K.count('1'))