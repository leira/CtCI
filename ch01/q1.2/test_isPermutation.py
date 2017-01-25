#!/usr/bin/env python3

def countChars(string):
    counts = {}
    for c in string:
        counts[c] = counts.get(c, 0) + 1
    return counts

# O(n)
def isPermutation(str1, str2):
    if len(str1) != len(str2):
        return False;

    counts1 = countChars(str1)
    counts2 = countChars(str2)
    return counts1 == counts2


def test_isPermutation():
    assert isPermutation('python', 'thonpy')
    assert isPermutation('', '')
    assert not isPermutation('python', 'honpy')
    assert not isPermutation('112345', '543221')

