def binary_search(data, target, low, high):
    if low > high:
        return False

    mid = (low + high) // 2
    if target == data[mid]:
        return mid
    elif target < data[mid]:
        return binary_search(data, target, low, mid - 1)
    else:
        return binary_search(data, target, mid + 1, high)


if __name__ == "__main__":
    lst = [3, 4, 8, 12, 42, 56, 88]
    print(binary_search(lst, 12, 0, len(lst) - 1))
    print(binary_search(lst, 20, 0, len(lst) - 1))