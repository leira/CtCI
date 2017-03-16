import sys
sys.path.append('..')
from node import Node, checkEqual

def getLoopPoint(head):
    if not head or not head.next:
        return None

    slow = head.next
    fast = head.next.next

    while slow != fast:
        if not fast or not fast.next:
            return None
        slow = slow.next
        fast = fast.next.next

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


def buildTestLoop(len, loopPoint):
    s = range(len)
    head, tail = Node.fromSeq(s)
    lp = head
    for i in range(loopPoint):
        lp = lp.next
    tail.next = lp
    return head


def test_getLoopPoint_NoLoop():
    assert getLoopPoint(None) == None

    s = range(17)
    l, _ = Node.fromSeq(s) 
    assert getLoopPoint(l) == None


def test_getLoopPoint_coughtInSingleLoop():
    l = buildTestLoop(17, 5)
    assert getLoopPoint(l).data == 5


def test_getLoopPoint_coughtInMultipleLoop():
    l = buildTestLoop(32, 24)
    assert getLoopPoint(l).data == 24

