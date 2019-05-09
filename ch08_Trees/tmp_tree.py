import matplotlib.pyplot as plt


class EulerTour:

    def __init__(self, tree):
        self._tree = tree

    def tree(self):
        return self._tree

    def execute(self):
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])

    def _tour(self, p, d, path):
        """Perform tour of subtree rooted at Position p.
        p   Position of current node being visited
        d   depth of p in the tree
        path    list of indices of children on path from root to p
        """
        self._hook_previsit(p, d, path)
        results = []
        path.append(0)
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path))
            path[-1] += 1
        path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_previsit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d, path, results):
        pass


class BinaryEulerTour(EulerTour):
    def _tour(self, p, d, path):
        results = [None, None]
        self._hook_previsit(p, d, path)
        if self._tree.left(p) is not None:
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d+1, path)
            path.pop()
        self._hook_invisit(p, d, path)
        if self._tree.right(p) is not None:
            path.append(1)
            results[1] = self._tour(self._tree.right(p), d+1, path)
            path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_invisit(self, p, d, path):
        pass


class BinaryLayout(BinaryEulerTour):
    def __init__(self, tree):
        super().__init__(tree)
        self._count = 0
        _, self.ax = plt.subplots(1, 1)

    def _hook_invisit(self, p, d, path):
        self._count += 1
        p.setX(self._count)
        p.setY(d)

    def _hook_postvisit(self, p, d, path, results):
        self.ax.plot(p._X, p._Y, 'ko', markerfacecolor='none')
        self.ax.text(p._X, p._Y, p._val)
        if p._left:
            self.ax.plot([p._left._X, p._X], [p._left._Y, p._Y], 'k-')
        if p._right:
            self.ax.plot([p._right._X, p._X], [p._right._Y, p._Y], 'k-')


class Tree:
    class _Node:
        def __init__(self, val, left=None, right=None, parent=None):
            self._val = val
            self._left = left
            self._right = right
            self._parent = parent
            self._X = None
            self._Y = None

        def __str__(self):
            return str(self._val)

        def setX(self, x):
            self._X = x

        def setY(self, y):
            self._Y = y

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._root

    def left(self, p):
        if p and p._left:
            return p._left

    def right(self, p):
        if p and p._right:
            return p._right

    def is_leaf(self, p):
        return (p._left is None) and (p._right is None)

    def is_empty(self):
        return len(self) == 0

    def add_root(self, node):
        if self._root:
            raise ValueError('root exists')
        self._root = self._Node(node)
        self._size = 1
        return self._root

    def add_left(self, p, node):
        if p._left is not None:
            raise ValueError('left child exist')
        n = self._Node(node, parent=p)
        p._left = n
        self._size += 1
        return n

    def add_right(self, p, node):
        if p._right is not None:
            raise ValueError('right child exist')
        n = self._Node(node, parent=p)
        p._right = n
        self._size += 1
        return n

    def attach(self, p, t1, t2):
        if self.is_leaf(p):
            p._left = t1._root
            t1._root._parent = p
            t1._root = None

            p._right = t2._root
            t2._root._parent = p
            t2._root = None

    def display(self):
        self._display(self._root)

    def _display(self, p, indent=0):
        print(2*indent*' ', p)
        if p._left:
            self._display(p._left, indent+1)
        if p._right:
            self._display(p._right, indent+1)

    def graphize(self):
        self.count = 1
        _, ax = plt.subplots(1, 1)
        self._graphize(ax, self._root, 1)
        plt.show()

    def _graphize(self, axis, p, depth):
        if p._left:
            self._graphize(axis, p._left, depth+1)

        self.count += 1
        p.setX(self.count)
        p.setY(depth)
        if p._right:
            self._graphize(axis, p._right, depth+1)
        axis.plot(p._X, p._Y, 'o', markerfacecolor='none')
        axis.text(p._X, p._Y, p._val)
        if p._left:
            axis.plot([p._left._X, p._X], [p._left._Y, p._Y], 'k-')
        if p._right:
            axis.plot([p._right._X, p._X], [p._right._Y, p._Y], 'k-')

    def pre_next(self, p):
        if p._left:
            return p._left
        else:
            cur = p
            while cur and cur._parent._right is cur:
                cur = cur._parent
                if not cur._parent:
                    return cur._parent
            return cur._parent._right

            # if p._right:
            #     return p._right
            # cur = p._parent
            # last = p
            # while cur and cur._right is last:
            #     last = cur
            #     cur = cur._parent
            # if cur:
            #     return cur._right
            # else:
            #     return None

    def post_next(self, p):
        if p._parent and p is p._parent._left:
            cur = p._parent
            last = p
            while cur:
                if cur._left and cur._left is not last:
                    cur = cur._left
                elif cur._right:
                    cur = cur._right
                else:
                    return cur
        else:
            return p._parent

    def inv_next(self, p):
        if p._right:
            cur = p._right
            while cur._left:
                cur = cur._left
            return cur
        else:
            cur = p
            while cur and cur._parent and cur._parent._right is cur:
                cur = cur._parent
            return cur._parent

    def create_from_str(self, s):
        """
        s: dict, 2 of ['pre', 'in', 'post'] should be in s as keys
        """
        if 'pre' not in s:
            self.parse_method = self.post_in
        elif 'in' not in s:
            self.parse_method = self.pre_post
        else:
            self.parse_method = self.pre_in

        root, ls, rs = self.parse_root(s)
        if len(list(ls.values())[0]) > 0:
            self.parse_left(root, ls)
        if len(list(rs.values())[0]) > 0:
            self.parse_right(root, rs)

    def parse_root(self, s):
        rts, ls, rs = self.parse_method(s)
        root = self._Node(rts)
        self._root = root
        return root, ls, rs

    def parse_left(self, p, s):
        s1, s2 = list(s.values())
        if len(s1) == 1 and s1 == s2:
            p._left = self._Node(s1, parent=p)
        else:
            rts, ls, rs = self.parse_method(s)
            node = self._Node(rts, parent=p)
            p._left = node
            if len(list(ls.values())[0]) > 0:
                self.parse_left(node, ls)
            if len(list(rs.values())[0]) > 0:
                self.parse_right(node, rs)

    def parse_right(self, p, s):
        s1, s2 = list(s.values())
        if len(s1) == 1 and s1 == s2:
            p._right = self._Node(s1, parent=p)
        else:
            rts, ls, rs = self.parse_method(s)
            node = self._Node(rts, parent=p)
            p._right = node
            if len(list(ls.values())[0]) > 0:
                self.parse_left(node, ls)
            if len(list(rs.values())[0]) > 0:
                self.parse_right(node, rs)

    @staticmethod
    def pre_post(s):
        """
        s1: pre str
        s2: post str
        """
        s1 = s['pre']
        s2 = s['post']
        rts = s1[0]
        ls = s1[1]
        li = s2.find(ls)
        ls1, ls2, rs1, rs2 = s1[1:2+li], s2[:li+1], s1[2+li:], s2[li+1:-1]
        return rts, {'pre': ls1, 'post': ls2}, {'pre': rs1, 'post': rs2}

    @staticmethod
    def pre_in(s):
        """
        s1: pre str
        s2: in str
        """
        s1 = s['pre']
        s2 = s['in']
        rts = s1[0]
        rti = s2.find(rts)
        ls1, ls2, rs1, rs2 = s1[1:1+rti], s2[:rti], s1[1+rti:], s2[rti+1:]
        return rts, {'pre': ls1, 'in': ls2}, {'pre': rs1, 'in': rs2}

    @staticmethod
    def post_in(s):
        """
        s1: post str
        s2: in str
        """
        s1 = s['post']
        s2 = s['in']
        rts = s1[-1]
        rti = s2.find(rts)
        ls1, ls2, rs1, rs2 = s1[:rti], s2[:rti], s1[rti:-1], s2[rti+1:]
        return rts, {'post': ls1, 'in': ls2}, {'post': rs1, 'in': rs2}


def is_isomorphic(T1, T2):
    return _is_isomorphic(T1, T1.root(), T2, T2.root()) > 0


def _is_isomorphic(T1, p1, T2, p2):
    if p1 is None or p2 is None:
        return False
    if T1.is_leaf(p1) or T2.is_leaf(p2):
        if T1.is_leaf(p1) and T2.is_leaf(p2):
            return True
        else:
            return False
    else:
        return _is_isomorphic(T1, T1.left(p1), T2, T2.left(p2)) + _is_isomorphic(T1, T1.right(p1), T2, T2.right(p2))


if __name__ == "__main__":
    # str_all = {'pre': 'MAXFUN', 'in': 'XAFMNU', 'post': 'XFANUM'}
    T1 = Tree()
    # T1.create_from_str({'pre': 'MAXFUN', 'in': 'XAFMNU'})
    # T1.create_from_str({'in': 'XAFMNU', 'post': 'XFANUM'})
    # T1.create_from_str({'pre': 'MAXFUN', 'post': 'XFANUM'})
    # T1.graphize()
    a = T1.add_root('A')
    b = T1.add_left(a, 'B')
    c = T1.add_right(a, 'C')
    d = T1.add_left(b, 'D')
    e = T1.add_right(b, 'E')
    f = T1.add_left(e, 'F')
    g = T1.add_right(e, 'G')
    # T1.graphize()
    print(T1.pre_next(a))
    print(T1.pre_next(b))
    print(T1.pre_next(c))
    print(T1.pre_next(d))
    print(T1.pre_next(e))
    print(T1.pre_next(f))
    print(T1.pre_next(g))


    # T2 = Tree()
    # r = T2.add_root(6)
    # l1 = T2.add_left(r, 4)
    # r1 = T2.add_right(r, 3)
    # # T2.add_right(r1, 8)
    # T2.display()

    # print(is_isomorphic(T1, T2))

    # T3 = Tree()
    # r = T3.add_root(7)

    # T3.attach(r, T1, T2)
    # # T3.display()
    # # T3.graphize()
    # b = BinaryLayout(T3)
    # b.execute()
    # plt.show()


