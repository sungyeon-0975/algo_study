import sys
input = sys.stdin.readline

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except ValueError:
        break

# 다른 사람 코드인데 아직 이해 못 한 상태
def postorder(start, end):
    if start >= end:
        return

    root = preorder[start]

    if preorder[end - 1] <= root:
        postorder(start + 1, end)
        print(root)
        return

    for i in range(start + 1, end):
        if preorder[i] > root:
            idx = i
            break

    postorder(start + 1, idx)
    postorder(idx, end)
    print(root)
    
postorder(0, len(preorder))


# 테스트 케이스만 정답
# temp = preorder.pop(0)
# postorder = []
# cnt = 1
# while cnt < len(preorder):
#     if preorder[cnt - 1] > preorder[cnt]:
#         cnt += 1
#         continue
    
#     postorder.append(preorder.pop(cnt-1))

#     try:
#         if preorder[cnt - 1] < preorder[cnt]:
#             postorder.append(preorder.pop(cnt-1))
#         cnt = 0
#     except IndexError:
#         postorder.append(temp)

# postorder.append(temp)
# for i in range(len(postorder)):
#     print(postorder[i])