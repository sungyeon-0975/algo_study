if __name__ == "__main__":
    res = [0]*10
    a,b,c = [int(input()) for _ in range(3)]
    #sol1
    result = a*b*c
    while result:
        res[result % 10] += 1
        result //= 10
        
    #sol2
    # result = str(a*b*c)
    # for s in result:
    #     res[int(s)] += 1
    #     pass
    
    print('\n'.join(map(str,res)))

