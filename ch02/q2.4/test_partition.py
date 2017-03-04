import sys
sys.path.append('..')
from node import Node, checkEqual

def partition(ll, v):
    if not ll: return None
    left = ll
    right = ll
    while right.next:
        node = right.next
        if node.data < v:
            right.next = node.next
            node.next = left
            left = node
        else:
            right = right.next
    return left

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

