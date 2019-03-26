class Empty(Exception):
    pass


class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """Raise Empty Exception if Queue is empty."""
        if self.is_empty():
            raise Empty('Queue is empty.')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty.')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size <= len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

    def __str__(self):

        lst = 'Queue<{}>'.format(', '.join(
            str(self._data[(self._front + i) % len(self._data)]) for i in range(self._size)))
        return lst


if __name__ == "__main__":
    Q = ArrayQueue()
    Q.enqueue(5)
    Q.enqueue(3)
    print(Q)
    print(len(Q))
    Q.dequeue()
    print(Q)
    print(Q.is_empty())
    Q.dequeue()
    print(Q.is_empty())
    try:
        Q.dequeue()
    except Exception as e:
        print(e)
    Q.enqueue(7)
    Q.enqueue(9)
    Q.first()
    Q.enqueue(4)
    print(Q)
    print(len(Q))
    Q.dequeue()
    print(Q)
