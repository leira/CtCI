import pytest

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __repr__(self):
        return '{0} -> {1}'.format(self.data, self.next)

    def insertSeq(self, seq):
        tail = self
        for e in seq:
            node = Node(e, None)
            tail.next = node
            tail = node

    @staticmethod
    def fromSeq(seq):
        fakeHead = Node(None, None)
        fakeHead.insertSeq(seq)
        return fakeHead.next

def partition(ll, v):
    if not ll: return None
    left = ll
    right = ll
#    pytest.set_trace()
    while right.next:
        node = right.next
        if node.data < v:
            right.next = node.next
            node.next = left
            left = node
        else:
            right = right.next
    return left

def checkEqual(ll, seq):
    i = 0
    node = ll
    while node:
        assert node.data == seq[i]
        i += 1
        node = node.next
    assert i == len(seq)

def test_fromSeq():
    seq = [1, 2, 3, 4, 5]
    head = Node.fromSeq(seq)
    checkEqual(head, seq)

def test_partition():
    seq = [3, 5, 8, 5, 10, 2, 1]
    ll = Node.fromSeq(seq)
    pl = partition(ll, 5)
    partitioned = [1, 2, 3, 5, 8, 5, 10]
    checkEqual(pl, partitioned)

    seq = [3, 5, 8, 5, 10]
    ll = Node.fromSeq(seq)
    pl = partition(ll, 10)
    partitioned = [5, 8, 5, 3, 10]
    checkEqual(pl, partitioned)

