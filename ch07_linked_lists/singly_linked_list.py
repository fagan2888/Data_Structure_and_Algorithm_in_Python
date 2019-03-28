class Empty(Exception):
    pass


class LinkedStack:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next=None):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        """O(1)"""
        return self._size

    def is_empty(self):
        """O(1)"""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack.
        O(1)
        """
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """O(1)"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        """O(1)"""
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
