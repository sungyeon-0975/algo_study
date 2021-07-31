if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        results = input()
        score = 0
        acc = 0
        for result in results:
            if result == 'O':
                acc += 1
                score += acc
            else:
                acc = 0
        print(score)

