#!/usr/bin/env python3

def isSameOrReplace(src, dest):
    for i in range(len(src)):
        if src[i] != dest[i]:
            return src[i+1:] == dest[i+1:]
    return True

def isInsert(src, dest):
    for i in range(len(src)):
        if src[i] != dest[i]:
            return src[i:] == dest[i+1:]
    return True

def isDelete(src, dest):
    for i in range(len(dest)):
        if src[i] != dest[i]:
            return src[i+1:] == dest[i:]
    return True

def isOneChangeAway(src, dest):
    lenDiff = len(src) - len(dest)
    if lenDiff == 0:
        return isSameOrReplace(src, dest)
    elif lenDiff == -1:
        return isInsert(src, dest)
    elif lenDiff == 1:
        return isDelete(src, dest)
    else:
        return False


def test_isOneChangeAway():
    assert isOneChangeAway('pale', 'ple')
    assert isOneChangeAway('pales', 'pale')
    assert isOneChangeAway('pale', 'bale')
    assert not isOneChangeAway('pale', 'bake')

    assert isOneChangeAway('pale', 'palee')
    assert isOneChangeAway('pale', 'pal')
    assert not isOneChangeAway('pale', 'paaale')

