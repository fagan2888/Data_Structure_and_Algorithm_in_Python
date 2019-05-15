from Priority_Queue import PriorityQueueBase


class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap.
    Heap-order property: In a heap T, for every position p other than the root, the key stored at p is greater than or equal to the key stored at p's parent。

    Complete Binary Tree Poperty: A heap T with height h is a complete binary tree if levels 0, 1, 2,..., h-1 of T have the maximum number of nodes possible (namely, level i has 2^i nodes, for 0 <= i <= (h-1)) and the remaining nodes at level h reside in the leftmost possible positions at that level.

    The height of a heap: A heap T storing n entris has height h = \\lfloor log(n) \\rfloor

    """

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(small_child, j)
                self._downheap(small_child)

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def add(self, key, value):
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)

    def min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        self._swap(0, len(self._data) - 1)              # put minimum item at the end
        item = self._data.pop()                         # and remove it from the list
        self._downheap(0)                               # then fix new root
        return (item._key, item._value)


class Empty(Exception):
    pass


if __name__ == "__main__":
    hpq = HeapPriorityQueue()
    hpq.add(8, 'hi')
    hpq.add(2, 'hi')
    hpq.add(1, 'hi')
    hpq.add(7, 'hi')
    hpq.add(7, 'hi')
    hpq.add(0, 'hi')
    print(hpq)
    print(hpq.min())
    hpq.remove_min()
    print(hpq)
    hpq.remove_min()
    print(hpq)
