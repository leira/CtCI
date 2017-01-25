#!/usr/bin/env python3

# using hash table, O(n)
def allUniq(string):
    chars = set(string)
    return len(chars) == len(string)


def test_allUniq():
    assert allUniq('python')
    assert not allUniq('1123345')
    assert not allUniq('stressful')
    assert not allUniq('  ')

