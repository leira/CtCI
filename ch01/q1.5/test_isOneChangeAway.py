#!/usr/bin/env python3

def isOneChangeAway(src, dest):
    lenDiff = len(src) - len(dest)
    if lenDiff > 1 or lenDiff < -1:
        return False;

    for i in range(min(len(src), len(dest))):
        if src[i] != dest[i]:
            if lenDiff == 0:    # replace
                return src[i+1:] == dest[i+1:]
            elif lenDiff == -1: # insert
                return src[i:] == dest[i+1:]
            if lenDiff == 1:    # delete
                return src[i+1:] == dest[i:]
    return True # same or one change in the end


def test_isOneChangeAway():
    assert isOneChangeAway('pale', 'ple')
    assert isOneChangeAway('pales', 'pale')
    assert isOneChangeAway('pale', 'bale')
    assert not isOneChangeAway('pale', 'bake')

    assert isOneChangeAway('pale', 'palee')
    assert isOneChangeAway('pale', 'pal')
    assert not isOneChangeAway('pale', 'paaale')

