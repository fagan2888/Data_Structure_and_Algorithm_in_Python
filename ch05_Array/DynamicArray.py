import ctypes
import copy


class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not -self._n <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None
                self._n -= 1
                if self._n <= self._capacity / 4:
                    self._resize(self._capacity / 2)
                return
        raise ValueError('value not found')

    def pop(self, *args):
        if len(args) == 0:
            tmp = copy.deepcopy(self._A[self._n - 1])
            self._A[self._n - 1] = None
            self._n -= 1
            if self._n <= self._capacity / 4:
                self._resize(self._capacity / 2)
            return tmp
        elif len(args) == 1:
            if isinstance(args[0], int):
                k = args[0]
                tmp = copy.deepcopy(self._A[k])
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None
                self._n -= 1
                if self._n <= self._capacity / 4:
                    self._resize(self._capacity / 2)
                return tmp
            else:
                raise TypeError('cannot be converted to integer')
        else:
            raise TypeError('takes at most 1 argument')

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def __str__(self):
        return '<' + ', '.join(str(self._A[ni]) for ni in range(self._n)) + '>'


if __name__ == "__main__":
    da = DynamicArray()
    for i in range(10):
        da.append(i)
    print(da)
    da.pop()
    print(da)
    da.pop(0)
    print(da)
    da.remove(3)
    print(da)
    da.insert(2, 99)
    print(da)
