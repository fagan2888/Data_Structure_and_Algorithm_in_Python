from Stack import ArrayStack


def is_matched(expr):
    left = '{(['
    right = '})]'
    S = ArrayStack()
    for c in expr:
        if c in left:
            S.push(c)
        elif c in right:
            if S.is_empty():
                return False
            elif right.index(c) != left.index(S.pop()):
                return False
    return S.is_empty()

if __name__ == "__main__":
    expr1 = '{}[]({[]})'
    expr2 = '{()}{[}]'
    expr3 = '(6+5) * (6+1)'
    print(is_matched(expr1))
    print(is_matched(expr2))
    print(is_matched(expr3))
