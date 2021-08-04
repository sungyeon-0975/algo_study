if __name__ == "__main__":
    n_a,n_b = map(int, input().split())
    A = set(input().split())
    B = set(input().split())
    print(len(A-B) + len(B-A))