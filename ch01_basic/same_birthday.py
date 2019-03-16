import random
from collections import Counter


def gen_birth(n):
    return [random.randint(1, 366) for i in range(n)]


def count(lst):
    return Counter(lst)


def find_same(cnt):
    return {k: v for k, v in cnt.items() if v > 1}

if __name__ == "__main__":
    for n in range(5, 105, 5):
        print(n, ": ", find_same(count(gen_birth(n))))

