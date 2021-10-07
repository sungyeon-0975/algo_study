"""
29200KB, 68ms


풀어본 뒤 인터넷에서 찾아본 의미
K = K-(K&((~K)+1))
(~K) + 1 = -K => -K가 뜻하는 바를 모르겠음

K = K - (K & -K)
Fenwick Tree를 알고 있으면 K & -K가 이진수에서 가장 뒤에 있는 1의 위치를 알아내는 것을 안다.

결국 문제에 주어진 식은 맨 뒤에 있는 1의 위치를 알아낸 후, 그 비트를 0으로 바꾸는 연산.
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