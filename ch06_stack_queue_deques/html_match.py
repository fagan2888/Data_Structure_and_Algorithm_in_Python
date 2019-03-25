from lxml import etree
from Stack import ArrayStack


def is_html_matched(raw):
    S = ArrayStack()
    j = raw.find('<')
    root = etree.Element("root")
    curr = root

    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return None
        tag = raw[j+1:k]

        if tag.startswith('/'):
            if S.is_empty():
                return False
            elif S.pop() != tag[1:]:
                return False
            curr = curr.getparent()
        else:
            curr = etree.SubElement(curr, tag)
            S.push(tag)

        j = raw.find('<', k+1)
    print(etree.tostring(root).decode('utf8'))
    return S.is_empty()


if __name__ == "__main__":
    html = """
    <body>
    <center>
    <h1> The Little Boat </h1>
    </center>
    <p> The storm tossed the little
    boat like a cheap sneaker in an
    old washing machine. The three
    drunken fishermen were used to
    such treatment, of course, but
    not the tree salesman, who even as
    a stowaway now felt that he
    had overpaid for the voyage. </p>
    </body>
    """
    print(is_html_matched(html))
