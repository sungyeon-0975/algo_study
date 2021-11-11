import sys
sys.stdin = open('11728_input.txt')
"""
184832KB, 1536ms
302108KB, 2324ms
"""
# N,M = map(int,input().split())
#
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
#
# answer = A+B
# answer = sorted(answer)
# print(*answer)

N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
answer = []

i,j=0,0

while i!=len(A) or j!=len(B):
    if i==len(A):
        answer.append(B[j])
        j+=1
    elif j==len(B):
        answer.append(A[i])
        i+=1
    else:
        if A[i]<B[j]:
            answer.append(A[i])
            i+=1
        else:
            answer.append(B[j])
            j+=1

print(" ".join(map(str,answer)))