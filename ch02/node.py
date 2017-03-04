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

    @staticmethod
    def fromSeq(seq):
        fakeHead = Node(None, None)
        fakeHead.insertSeq(seq)
        return fakeHead.next

def checkEqual(ll, seq):
    i = 0
    node = ll
    while node:
        assert node.data == seq[i]
        i += 1
        node = node.next
    assert i == len(seq)

