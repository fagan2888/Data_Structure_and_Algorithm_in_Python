from binary_tree import BinaryTree
from Queue import ArrayQueue
from euler_tour import PreorderPrintIndentedTour, PreorderPrintIndentedLabeledTour, ParenthesizeTour


class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

        def __str__(self):
            return 'Node(%s)' % str(self._element)

        __repr__ = __str__

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __str__(self):
            return 'Pos(%s)' % self._node.__str__()

        __repr__ = __str__

    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            print(p)
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        """Return position represented node"""
        return self._make_position(self._root)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return number of children
        p = position represented node
        """
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node    # convention for deprecated node
        return node._element

    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None     # set t1 instance to empty
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None     # set t2 instance to empty
            t2._size = 0

    def display(self):
        cur = self.root()
        self._display(cur, num=0)

    def _display(self, p, num):
        str_ = '-' * num
        print(str_ + str(p.element()))
        if self.left(p):
            self._display(self.left(p), num+1)
        if self.right(p):
            self._display(self.right(p), num+1)

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def positions(self):
        # return self.preorder()
        # make inorder the default
        return self.inorder()

    def breadthfirst(self):
        if not self.is_empty():
            fringe = ArrayQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)

    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other

        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other


def preorder_indent(T, p, d):
    print(2*d*' ' + str(p.element()))
    for c in T.children(p):
        preorder_indent(T, c, d+1)


def preorder_label(T, p, d, path):
    label = '.'.join(str(j+1) for j in path)
    print(2*d*' ' + label, str(p.element()))
    path.append(0)
    for c in T.children(p):
        preorder_label(T, c, d+1, path)
        path[-1] += 1
    path.pop()


def parenthesize(T, p):
    print(p.element(), end='')
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = '(' if first_time else ','
            print(sep, end='')
            first_time = False
            parenthesize(T, c)
        print(')', end='')


if __name__ == "__main__":
    T_root = LinkedBinaryTree()
    root = T_root._add_root(3)
    l1 = T_root._add_left(root, 4)
    r1 = T_root._add_right(root, 5)
    T_root._add_left(l1, 8)
    T_root._add_right(l1, 9)
    T_root._add_left(r1, 82)
    T_root.display()
    l = T_root.left(root)
    r = T_root.right(root)
    for c in T_root.children(root):
        print(c)
    preorder_indent(T_root, T_root.root(), 0)
    print('preorder_label')
    preorder_label(T_root, T_root.root(), 0, [])
    parenthesize(T_root, T_root.root())
    print('PreorderPrintIndentedTour')
    tour = PreorderPrintIndentedTour(T_root)
    tour.execute()
    print('PreorderPrintIndentedLabeledTour')
    tour = PreorderPrintIndentedLabeledTour(T_root)
    tour.execute()
    print('ParenthesizeTour')
    tour = ParenthesizeTour(T_root)
    tour.execute()
