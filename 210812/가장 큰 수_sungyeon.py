import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return  (int(t1) < int(t2)) - (int(t1) > int(t2))
#  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator))
    answer = str(int(''.join(n)))
    return answer


# from collections import deque

# def solution(numbers):
#     l=deque(sorted(list(map(str,numbers)), key=lambda x: (x[0],converse(x),converse1(x))))
#     # print(l)
#     answer = int(merge1(l))
#     return str(answer)

# def converse(x):
#     y=x[0]
#     return (x+y+y+y)[:5]

# def converse1(x):
#     y=x[len(x)-1]
#     return (x+y+y+y)[:5]

# def merge1(l):
#     s=''
#     while l:
#         x=l.popleft()
#         s=x+s
#     return s