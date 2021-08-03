import sys # 아직 sys 잘 모르겠는데 기솔언니가 알려줌^^
input = sys.stdin.readline

num = int(input())
count = 0

def check(num):
    numdigit = str(num)
    if int(numdigit[0]) - int(numdigit[1]) == int(numdigit[1]) - int(numdigit[2]):
        return True
    else:
        return False

for n in range(1, num+1):
    if n < 100:
        count += 1
    elif check(n):
        count += 1
print(count)