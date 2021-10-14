'''
568ms
'''

if __name__ == "__main__":
    n = int(input())
    l = [-1, 0] + [0]*(n-1)
    i = 2
    for i in range(2, n + 1):
        min_val = l[i-1]
        if i % 2 == 0 and min_val > l[i//2]:
            min_val = l[i//2]
        if i % 3 == 0 and min_val > l[i//3]:
            min_val = l[i//3]
        l.append(min_val+1)
    
    print(l[-1])


'''
632ms
'''
# if __name__ == "__main__":
#     n = int(input())
#     l = [-1, 0]
#     i = 2
#     for i in range(2, n + 1):
#         l.append(min(l[i-1], l[i//2] if i%2 == 0 else i, l[i//3] if i%3 == 0 else i) + 1)
#     print(l[-1])
