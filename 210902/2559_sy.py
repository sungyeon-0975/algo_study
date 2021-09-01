if __name__ == "__main__":
    n,k = map(int, input().split())
    temperature = list(map(int, input().split())) 
    val = sum(temperature[:k])
    max_val = val
    s = 0
    for e in range(k,n):
        val = val  - temperature[s] + temperature[e]
        if val > max_val :
            max_val = val
        s += 1
    
    print(max_val)