def is_odd(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 1:
            for j in range(i+1, len(lst)):
                if lst[j] % 2 == 1 and lst[i] != lst[j]:
                    return lst[i], lst[j]
    return None, None

if __name__ == '__main__':
    a = [12, 1, 1, 4, 3]
    x, y = is_odd(a)
    print(x, y)
