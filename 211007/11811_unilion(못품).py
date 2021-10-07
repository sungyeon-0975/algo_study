"""
29200KB, 68ms
"""

N = int(input())
K = int(input(),2)
result = 0
while K:
    K = K-(K&((~K)+1))
    # if len(str(K)) >= 17:
    #     K=int(str(K)[1:17])
    result += 1
print(result)