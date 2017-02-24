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


def eraseNode(node):
    assert node and node.next
    next = node.next
    node.data, next.data = next.data, node.data
    node.next = next.next
    next.next = None
    return next

def checkEqual(ll, seq):
    i = 0
    node = ll
    while node:
        assert node.data == seq[i]
        i += 1
        node = node.next
    assert i == len(seq)

def test_eraseNode():
    seq = [1, 2, 3, 4, 5, 6, 7]
    ll = Node.fromSeq(seq)

    seq.remove(5)
    node = ll
    while node.data != 5:
        node = node.next
    assert eraseNode(node).data == 5

    checkEqual(ll, seq)

