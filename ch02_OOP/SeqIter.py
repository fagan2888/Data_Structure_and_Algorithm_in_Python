class SequenceIterator:

    def __init__(self, seq):
        self._seq = seq
        self._k = -1

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        return self

if __name__ == "__main__":
    seq = SequenceIterator([1, 4, 6])
    for e in seq:
        print(e)