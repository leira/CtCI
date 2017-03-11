import sys
sys.path.append('..')
from node import Node, checkEqual

def sumList(l1, l2):
    fh = Node(None, None)
    p = [l1, l2]
    r = fh
    carry = 0
    while p[0] or p[1]:
        d = [0, 0]
        for i in range(2):
            if p[i]:
                d[i] = p[i].data
                p[i] = p[i].next
        carry, s = divmod(sum(d)+carry, 10)
        r = r.insertAfter(Node(s, None))
    if carry:
        r = r.insertAfter(Node(carry, None))
    return fh.next

def test_eraseNode():
    s1 = [7, 1, 6]
    l1, _ = Node.fromSeq(s1)
    s2 = [5, 9, 2]
    l2, _ = Node.fromSeq(s2)
    lr = sumList(l1, l2)
    r = [2, 1, 9]
    checkEqual(lr, r)

    s1 = [7, 1, 6]
    l1, _ = Node.fromSeq(s1)
    s2 = [5, 9, 4]
    l2, _ = Node.fromSeq(s2)
    lr = sumList(l1, l2)
    r = [2, 1, 1, 1]
    checkEqual(lr, r)

