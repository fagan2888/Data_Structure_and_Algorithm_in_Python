class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class ArrayStack:
    """LIFO Stack Implementation using a python list"""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()


def reverse_file(file_name):
    S = ArrayStack()
    with open(file_name, 'r') as f:
        for line in f:
            S.push(line.rstrip('\n'))

    with open(file_name, 'w') as f:
        while not S.is_empty():
            f.write(S.pop() + '\n')


if __name__ == "__main__":
    S = ArrayStack()
    S.push(5)
    S.push(3)
    print(len(S))
    print(S.pop())
    print(S.is_empty())
    print(S.pop())
    print(S.is_empty())
    S.push(7)
    S.push(9)
    print(S.top())
    S.push(4)
    print(len(S))
    print(S.pop())
    S.push(6)

    reverse_file('tt')