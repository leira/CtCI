import sys
sys.path.append('..')
from node import Node, checkEqual

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

def test_eraseNode():
    s = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    l, _ = Node.fromSeq(s)
    assert isPalindrome(l)

    s = [1, 2, 3, 4, 5, 3, 2, 1]
    l, _ = Node.fromSeq(s)
    assert not isPalindrome(l)

