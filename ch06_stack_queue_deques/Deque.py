class Empty(Exception):
    pass


class Deque:
    DEFAULT_SIZE = 10

    def __init__(self):
        self._data = [None] * Deque.DEFAULT_SIZE
        self._front = 0
        self._size = 0

    def add_first(self, e):
        len_data = len(self._data)
        if self._size == len_data:
            self._resize(2 * len_data)
        avail = (self._front + len_data - 1) % len_data
        self._data[avail] = e
        self._front = avail
        self._size += 1

    def add_last(self, e):
        len_data = len(self._data)
        if self._size == len_data:
            self._resize(2 * len_data)
        avail = (self._front + self._size) % len_data
        self._data[avail] = e
        self._size += 1

    def delete_first(self):
        if self.is_empty():
            raise Empty('Queue is empty.')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size <= len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def delete_last(self):
        if self.is_empty():
            raise Empty('Queue is empty.')
        answer = self._data[(self._front + self._size - 1) % len(self._data)]
        self._data[(self._front + self._size - 1) % len(self._data)] = None
        self._size -= 1
        if 0 < self._size <= len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def first(self):
        """Return (but do not remove) the first elemtent of deque;
        an error occurs if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty.')
        return self._data[self._front]

    def last(self):
        """Return (but do not remove) the last elemtent of deque;
        an error occurs if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty.')
        return self._data[(self._front + self._size - 1) % len(self._data)]

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

    def __str__(self):
        lst = 'Deque<{}>'.format(', '.join(
            str(self._data[(self._front + i) % len(self._data)]) for i in range(self._size)))
        return lst


if __name__ == "__main__":
    D = Deque()
    D.add_last(5)
    D.add_first(3)
    print(D)
    D.add_first(7)
    print(D)
    print(D.first())
    D.delete_last()
    print(D)
    print(len(D))
    D.delete_last()
    print(D)
    D.delete_last()
    try:
        D.delete_last()
    except Exception as e:
        print('Error:', e)
    print(D)
    D.add_first(6)
    print(D.last())
    D.add_first(8)
    print(D.is_empty())
    print(D.last())
    print(D)
