def puzzle(k, S, U):
    for e in U:
        U.remove(e)
        S.append(e)
        if k == 1:
            if test(S):
                print("Solution found: ", S)
        else:
            puzzle(k-1, S, U)
        print(S)
        S.remove(e)
        U.add(e)


def test(S):
    # print(S)
    b, o, y, g, i, r, l, a = S[:8]
    res = 100 * b + 10 * o + y + 1000 * g + 100 * i + \
        10 * r + l == 1000 * b + 100 * a + 10 * b + y
    if res:
        print(100 * b + 10 * o + y, ' + ', 1000 * g + 100 * i +
              10 * r + l, ' = ', 1000 * b + 100 * a + 10 * b + y)
    return res


if __name__ == "__main__":
    S = []
    U = set(range(10))
    print(puzzle(8, S, U))
