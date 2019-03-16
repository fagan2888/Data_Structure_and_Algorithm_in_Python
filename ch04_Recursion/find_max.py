def find_max(seq, start, end):
    """find the maximum num in seq[start:end]"""
    if start == end - 1:
        return seq[start]
    mid = (start + end) // 2
    left = find_max(seq, start, mid)
    right = find_max(seq, mid, end)
    if left >= right:
        return left
    else:
        return right

if __name__ == "__main__":
    s = [5, 6, 9, 10, 23, -2, 100]
    print(find_max(s, 0, len(s)))
