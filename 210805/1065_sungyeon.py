if __name__ == "__main__":
    n = int(input())
    cnt = 0
    for i in range(1,n+1):
        new = i % 100
        i //= 100
        old = new%10
        new //= 10
        inter = old - new
        old = new
        while i:
            new = i % 10
            i //= 10
            if old-new == inter:
                continue
            else:
                cnt += 1
                break
         
    print(n-cnt)



            