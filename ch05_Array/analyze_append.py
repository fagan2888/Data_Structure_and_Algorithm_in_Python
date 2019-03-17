from time import time


def compute_average(n):
    data = []
    start = time()

    for _ in range(n):
        data.append(None)
    end = time()
    return (end - start) / n

if __name__ == "__main__":
    print(compute_average(100))
