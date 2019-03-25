import random


def shuffle(lst):
    for i in range(len(lst)):
        k = random.randrange(len(lst))
        lst[i], lst[k] = lst[k], lst[i]


if __name__ == "__main__":
    a = [3, 1, 4, 5, 9]
    shuffle(a)
    print(a)
