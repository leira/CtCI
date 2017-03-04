import sys
sys.path.append('..')
from node import Node, checkEqual

def getIntersection(l1, l2):
    s = [0, 0]
    p = [l1, l2]
    for i in range(2):
        while p[i].next:
            p[i] = p[i].next
            s[i] += 1
    if p[0] is not p[1]:
        return None
    p = [l1, l2]
    for i in range(s[0] - s[1]):
        p[0] = p[0].next
    for i in range(s[1] - s[0]):
        p[1] = p[1].next
    while p[0] and p[1]:
        if p[0] is p[1]:
            return p[0]
        p[0] = p[0].next
        p[1] = p[1].next
    return None

def test_eraseNode():
    s1 = [1, 2, 3, 4, 5]
    fh = Node(None, None)
    fh.insertSeq(s1)
    checkEqual(fh.next, s1)
    l1 = fh.next
    p1 = l1.next
    p1 = p1.next
    assert p1.data == 3

    l2 = Node(10, None)
    p2 = l2.insertAfter(Node(11, None))
    p2 = p2.insertAfter(Node(12, None))
    p2.next = p1
    assert getIntersection(l1, l2) is p1

    s1 = [1, 2, 3, 4, 5]
    fh = Node(None, None)
    fh.insertSeq(s1)
    l1 = fh.next
    fh = Node(None, None)
    fh.insertSeq(s1)
    l2 = fh.next
    assert not getIntersection(l1, l2)

