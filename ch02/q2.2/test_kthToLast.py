import sys
sys.path.append('..')
from node import Node, checkEqual

def kthToLast(head, k):
    if k == 0:
        return None
    ahead = head
    for i in range(k):
        if not ahead:
            return None
        ahead = ahead.next
    kth = head
    while ahead:
        ahead = ahead.next
        kth = kth.next
    return kth

def test_kthToLast():
    ll = Node.fromSeq([1, 2, 3, 4, 5, 6, 7]);
    assert kthToLast(ll, 3).data == 5
    assert kthToLast(ll, 1).data == 7
    assert kthToLast(ll, 7).data == 1
    assert kthToLast(ll, 8) == None
    assert kthToLast(ll, 0) == None

    assert kthToLast(None, 5) == None

