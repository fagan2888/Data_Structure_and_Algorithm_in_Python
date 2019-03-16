def hanoi(n, from_, mid, to):
    if n == 1:
        print('moving from ', from_, ' to ', to)
    else:
        hanoi(n - 1, from_, to, mid)
        print('moving from ', from_, ' to ', to)
        hanoi(n - 1, mid, from_, to)


if __name__ == "__main__":
    hanoi(3, 'A', 'B', 'C')
