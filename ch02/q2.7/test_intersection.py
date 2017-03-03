import pytest

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __repr__(self):
        return '{0} -> {1}'.format(self.data, self.next)

    def insertAfter(self, node):
        node.next = self.next
        self.next = node
        return node

    def insertSeq(self, seq):
        tail = self
        for e in seq:
            node = Node(e, None)
            tail = tail.insertAfter(node)

def haveIntersection(l1, l2):
    p = [l1, l2]
    for i in range(2):
        while p[i].next:
            p[i] = p[i].next
    return p[0] is p [1]

def checkEqual(ll, seq):
    i = 0
    node = ll
    while node:
        assert node.data == seq[i]
        i += 1
        node = node.next
    assert i == len(seq)

def test_insertSeq():
    s1 = [1, 2, 3, 4, 5]
    fh = Node(None, None)
    fh.insertSeq(s1)
    checkEqual(fh.next, s1)


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
    assert haveIntersection(l1, l2)

    s1 = [1, 2, 3, 4, 5]
    fh = Node(None, None)
    fh.insertSeq(s1)
    l1 = fh.next
    fh = Node(None, None)
    fh.insertSeq(s1)
    l2 = fh.next
    assert not haveIntersection(l1, l2)

