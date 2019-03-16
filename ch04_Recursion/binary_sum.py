def binary_sum(S, start, end):
    if start >= end:
        return 0
    elif start == end - 1:
        return S[start]
    else:
        mid = (start + end) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, end)


if __name__ == "__main__":
    print(binary_sum(range(10), 0, 10))
