start = int(input())
max_length = 1  # 자기자신은 무조건 반환
max_list = [start]
for i in range(start + 1):  # 적힌 숫자와 같아질때까지 0 더해짐
    data = [start, i]  # 하나씩 검색
    j = 0
    while True:
        result = data[j] - data[j + 1]  #
        if result < 0:  # 두값의 차이가 음수라면
            break  # 중지
        data.append(result)  # 아니면 더해준다

        if max_length < len(data):  # 전체 맥스길이 찾고
            max_length = len(data)
            max_list = data[:]  # 그 당시의 리스트를 복사

        j += 1
print(max_length)
print(*max_list)

# n = int(input())
# q = [0, 0]
# for i in range(n // 2, n + 1):
#     x, y = n, i
#     c = 2
#     while 1:
#         x, y = y, x - y
#         if y < 0: break
#         c += 1
#     if c > q[0]: q = [c, i]
# x, y = n, q[1]
# w = [x, y]
# while 1:
#     x, y = y, x - y
#     if y < 0: break
#     w += [y]
# print(len(w))
# print(*w)
