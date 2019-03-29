class Empty(Exception):
    pass


class CircularQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next=None):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = head._next
        self._size -= 1
        return head._element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next

    def __str__(self):
        if self._size == 0:
            return '<>'
        cur = self._tail._next
        str_ = [str(cur._element)]
        while cur is not self._tail:
            cur = cur._next
            str_.append(str(cur._element))
        return '<' + ','.join(str_) + '>'

if __name__ == "__main__":
    cq = CircularQueue()
    print(cq)
    cq.enqueue(5)
    print(cq)
    cq.enqueue(3)
    print(cq)
    cq.enqueue(4)
    print(cq)
    cq.rotate()
    cq.rotate()
    print(cq)
    cq.dequeue()
    print(cq)
    cq.dequeue()
    print(cq)
