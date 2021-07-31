if __name__ == "__main__":
    num = int(input())
    cycle = 0
    new = num
    while True:
        old = new
        new = old%10*10 + (old//10+old) % 10
        cycle += 1
        if new == num:
            break
    print(cycle)
    






