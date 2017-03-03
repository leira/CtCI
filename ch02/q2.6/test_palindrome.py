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


def isPalindrome(l):
    stack = []
    p = l
    while p:
        stack.append(p.data)
        p = p.next
    p = l
    while p:
        if p.data != stack.pop():
            return False
        p = p.next
    return True

def checkEqual(ll, seq):
    i = 0
    node = ll
    while node:
        assert node.data == seq[i]
        i += 1
        node = node.next
    assert i == len(seq)

def test_eraseNode():
    s = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    l = Node.fromSeq(s)
    assert isPalindrome(l)

    s = [1, 2, 3, 4, 5, 3, 2, 1]
    l = Node.fromSeq(s)
    assert not isPalindrome(l)

