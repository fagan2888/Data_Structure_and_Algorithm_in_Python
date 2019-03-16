def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k

if __name__ == '__main__':
    n = int(input('Enter an positive integer:'))
    for k in factors(n):
        print(k)
