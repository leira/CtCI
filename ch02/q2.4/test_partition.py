class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def insertAfter(self, node):
        node.next = self.next
        node.prev = self
        if self.next:
            self.next.prev = node
        self.next = node
        return node

    @staticmethod
    def fromSeq(seq):
        head = None
        prev = None
        for e in seq:
            node = Node(e)
            if not head:
                head = node
            if prev:
                prev.insertAfter(node)
            prev = node
        return head

    @staticmethod
    def swap(n1, n2):
        if n1.prev:
            n1.prev.next = n2
        if n1.next:
            n1.next.prev = n2
        if n2.prev:
            n2.prev.next = n1
        if n2.next:
            n2.next.prev = n1
        n1.prev, n1.next, n2.prev, n2.next = \
        n2.prev, n2.next, n1.prev, n1.next


def partition(ll, v):
    rh = ll
    while (rh and rh.data < v):
        rh = rh.next
    if not rh:
        return

    sh = rh.next
    while (sh):
        if sh.data < v:
            Node.swap(sh, rh)
            rh, sh = sh.next, rh.next
        else:
            sh = sh.next


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
    partition(ll, 5)
    partitioned = [3, 2, 1, 5, 10, 5, 8]
    checkEqual(ll, partitioned)

    seq = [3, 5, 8, 5, 10]
    ll = Node.fromSeq(seq)
    partition(ll, 10)
    checkEqual(ll, seq)

