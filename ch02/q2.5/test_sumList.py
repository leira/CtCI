import pytest

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def insertAfter(self, node):
        node.next = self.next
        self.next = node
        return node

    @staticmethod
    def fromSeq(seq):
        head = None
        prev = None
        for e in seq:
            node = Node(e, None)
            if not head:
                head = node
            if prev:
                prev.insertAfter(node)
            prev = node
        return head


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

def checkEqual(ll, seq):
    i = 0
    node = ll
    while node:
        assert node.data == seq[i]
        i += 1
        node = node.next
    assert i == len(seq)

def test_eraseNode():
    s1 = [7, 1, 6]
    l1 = Node.fromSeq(s1)
    s2 = [5, 9, 2]
    l2 = Node.fromSeq(s2)
    lr = sumList(l1, l2)
    r = [2, 1, 9]
    checkEqual(lr, r)

    s1 = [7, 1, 6]
    l1 = Node.fromSeq(s1)
    s2 = [5, 9, 4]
    l2 = Node.fromSeq(s2)
    lr = sumList(l1, l2)
    r = [2, 1, 1, 1]
    checkEqual(lr, r)

