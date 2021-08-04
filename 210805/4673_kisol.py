result = set()

for num in range(1, 10001):
    new_num = num
    while num > 0:
        new_num += num % 10
        num //= 10
    result.add(new_num)

for num in range(1, 10001):
    if num not in result:
        print(num)
