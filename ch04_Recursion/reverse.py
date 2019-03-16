def reverse(S, st, end):
    if st < end - 1:
        S[st], S[end-1] = S[end-1], S[st]
        reverse(S, st+1, end-1)


if __name__ == "__main__":
    s = [5, 3, 2, 0, 1]
    print(s)
    reverse(s, 0, len(s))
    print(s)

