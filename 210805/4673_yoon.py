numbers = set()

def d(num):
    new_num = n + n//1000 + (n//100)%10 + (n//10)%10 + n%10
    if new_num <= 10000:
        numbers.add(new_num)

for n in range(1, 10000):
    d(n)

ten_thousand = [x for x in range(1, 10001)]
for self_num in list(numbers):
    ten_thousand.remove(self_num)

for ans in ten_thousand:
    print(ans)