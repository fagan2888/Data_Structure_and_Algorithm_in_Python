import time


def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n - 2) + bad_fibonacci(n - 1)


def good_fibonacci(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n - 1)
        return (a + b, a)

if __name__ == "__main__":
    t = time.process_time()
    print(good_fibonacci(37))
    print(time.process_time() - t)

    t = time.process_time()
    print(bad_fibonacci(37))
    print(time.process_time() - t)
