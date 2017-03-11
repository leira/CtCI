from node import Node, checkEqual

def test_insertSeq():
    s = [1, 2, 3, 4, 5]
    ll, _ = Node.fromSeq(s)
    checkEqual(ll, s)

