#!/usr/bin/env python3

def isPalinPerm(inStr):
    tracker = set()
    for c in inStr:
        c = c.lower()
        if not c.isalpha():
            continue
        elif c in tracker:
            tracker.remove(c)
        else:
            tracker.add(c)
    if len(tracker) > 1:
        return False
    else:
        return True

def test_isPalinPerm():
    assert isPalinPerm('Tact Coa')
    assert isPalinPerm("\tarray")
    assert not isPalinPerm("Palindrome")

