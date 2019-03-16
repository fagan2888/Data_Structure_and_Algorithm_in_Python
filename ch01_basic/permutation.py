def permutation(lst):
    if len(lst) == 0:
        yield lst
    for i, num in enumerate(lst):
        for nlst in permutation(lst[:i] + lst[i+1:]):
            yield [num] + nlst

if __name__ == "__main__":
    print(list(permutation([1, 2, 4])))
