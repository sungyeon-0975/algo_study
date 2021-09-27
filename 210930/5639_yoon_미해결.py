import sys
# input = sys.stdin.readline
sys.stdin = open('input_5639.txt')

'''
아무래도 테스트케이스만 맞는듯
'''

def post_order(node):
    if left[node]:
        post_order(left[node])
    if right[node]:
        post_order(right[node])
    print(pre_order[node])


pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    except:
        break

N = len(pre_order)
left = [0] * N
right = [0] * N

for n in range(1, N):
    if pre_order[n] < pre_order[n-1]:
        left[n-1] = n
    else:
        for k in range(n-1):
            if pre_order[k+1] < pre_order[n] < pre_order[k]:
                right[k+1] = n
                break
            elif right[k] == 0 and pre_order[0] <= pre_order[k] < pre_order[n]:
                right[k] = n
                break


post_order(0)