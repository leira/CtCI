import sys
sys.path.append('..')
from node import Node, checkEqual

def eraseNode(node):
    assert node and node.next
    next = node.next
    node.data, next.data = next.data, node.data
    node.next = next.next
    next.next = None
    return next

def test_eraseNode():
    seq = [1, 2, 3, 4, 5, 6, 7]
    ll = Node.fromSeq(seq)

    seq.remove(5)
    node = ll
    while node.data != 5:
        node = node.next
    assert eraseNode(node).data == 5

    checkEqual(ll, seq)

