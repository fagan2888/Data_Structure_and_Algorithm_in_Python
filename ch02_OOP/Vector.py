class Vector:

    def __init__(self, n):
        if isinstance(n, int):
            if n < 1:
                raise ValueError("n should not be less than 1.")
            self._v = [0] * n
        elif isinstance(n, list):
            self._v = n
        elif isinstance(n, Vector):
            self._v = n._v
        else:
            raise NotImplementedError('Not implemented for the input')

    def __setitem__(self, k, v):
        if k >= len(self._v):
            raise KeyError("out of boundary.")
        self._v[k] = v

    def __getitem__(self, k):
        return self._v[k]

    def __add__(self, other):
        if len(self._v) != len(other._v):
            raise ValueError("length not equal.")
        tmp = Vector(len(self._v))
        tmp._v = [i + j for i, j in zip(self._v, other._v)]
        return tmp

    def __sub__(self, other):
        if len(self._v) != len(other._v):
            raise ValueError("length not equal.")
        tmp = Vector(len(self._v))
        tmp._v = [i - j for i, j in zip(self._v, other._v)]
        return tmp

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self._v) != len(other._v):
                raise ValueError("length not equal.")
            tmp = sum([i * j for i, j in zip(self._v, other._v)])
        elif isinstance(other, (int, float)):
            tmp = Vector(len(self._v))
            tmp._v = [i * other for i in self._v]
        else:
            return NotImplemented

        return tmp

    def __rmul__(self, other):
        return self.__mul__(other)

    def __neg__(self):
        tmp = Vector(len(self._v))
        tmp._v = [-v for v in self._v]
        return tmp

    def __len__(self):
        return len(self._v)

    def __repr__(self):
        return '<' + ', '.join([str(k) for k in self._v]) + '>'


if __name__ == "__main__":
    v = Vector(5)
    v[1] = 23
    v[-1] = 45
    print(v[4])
    u = v + v
    print(u)
    print(-u)
    print(u * 3)
    print(3 * u)
    print(v * (-v))
    print(Vector([5, 7, 9]))
    print(Vector(u))

    total = 0

    for e in v:
        total += e

    print(total)
