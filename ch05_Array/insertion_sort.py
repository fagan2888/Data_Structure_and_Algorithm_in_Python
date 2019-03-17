def insertion_sort(A):
    """ input: An array A of n comparable elements
        output: The array with elements rearranged in nondecreasing order
        for k from 1 to n - 1 do
            insert A[k] at its proper location within A[0:k+1]
    """
    # for k in range(1, len(A)):
    #     for i in range(k-1, -1, -1):
    #         if A[i + 1] < A[i]:
    #             A[i+1], A[i] = A[i], A[i+1]
    #         else:
    #             break

    for k in range(1, len(A)):
        tmp = A[k]
        j = k
        while j > 0 and A[j-1] > tmp:
            A[j] = A[j-1]
            j -= 1
        A[j] = tmp



if __name__ == "__main__":
    lst = [5, 4, 7, 1, 12, 13, 23, 0, 4]
    print(lst)
    insertion_sort(lst)
    print(lst)
