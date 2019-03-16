def few(change, avail=(5, 2, 1)):
    if change < 1:
        return None

    ans = {}
    for a in avail:
        if change == 0:
            break
        n, change = divmod(change, a)
        ans[a] = n
    return ans

if __name__ == "__main__":
    res = few(5)
    print(res)