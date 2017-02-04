#!/usr/bin/env python3

def isRotation(src, dest):
    if len(src) != len(dest):
        return False;

    doubleSrc = src * 2
    return dest in doubleSrc


def test_isRotation():
    assert isRotation('waterbottle', 'erbottlewat')
    assert not isRotation('waterbottle', 'erbottlew')
    assert not isRotation('waterbottle', 'erbottlewac')

