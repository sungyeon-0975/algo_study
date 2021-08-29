if __name__ == "__main__":
    n = int(input())
    a, b, i = 1, 1, 0
    x_range = [n, -1]

    while int(x_range[0]) >= x_range[1]:
        a, b = b, a + b
        i += 1
        x_range[i % 2] = (a / b) * n
    x_range[i % 2] = (2 * a - b) / (b - a) * n
    x = int(x_range[0])
    res = [n, x]
    for j in range(i, 0, -1):
        res.append(res[-2] - res[-1])
    print(i + 2)
    print(*res)
