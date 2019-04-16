class Empty(Exception):
    pass


class _DoublyLinkedBase:
    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next_):
            self._element = element
            self._prev = prev
            self._next = next_

        def __str__(self):
            if self._element:
                return str(self._element)
            else:
                return ''

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def __str__(self):
        str_ = []
        # if self._size == 0:
        #     return '<>'
        cur = self._header._next
        while cur._next is not None:
            str_.append(str(cur._element))
            cur = cur._next
        return '<' + ','.join(str_) + '>'


class LinkedDeque(_DoublyLinkedBase):

    def first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev._element

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        self._delete_node(self._trailer._prev)


def find_middle(ld):
    if len(ld) == 0:
        return None
    if len(ld) % 2 == 0:
        left = ld._header
        right = ld._trailer._prev
    else:
        left = ld._header
        right = ld._trailer

    while left != right:
        left = left._next
        right = right._prev

    return left

if __name__ == "__main__":
    ld = LinkedDeque()
    # for i in range(10):
    #     ld.insert_first(i)
    print(find_middle(ld))
