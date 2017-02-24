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


def kthToLast(head, k):
    if k == 0:
        return None
    ahead = head
    for i in range(k):
        if not ahead:
            return None
        ahead = ahead.next
    kth = head
    while(ahead):
        ahead = ahead.next
        kth = kth.next
    return kth


def test_fromSeq():
    seq = [1, 2, 3, 4, 5]
    head = Node.fromSeq(seq);
    i = 0
    node = head
    while node:
        assert node.data == seq[i]
        i += 1
        node = node.next

def test_kthToLast():
    ll = Node.fromSeq([1, 2, 3, 4, 5, 6, 7]);
    assert kthToLast(ll, 3).data == 5
    assert kthToLast(ll, 4).data == 4
    assert kthToLast(ll, 7).data == 1
    assert kthToLast(ll, 8) == None
    assert kthToLast(ll, 0) == None

