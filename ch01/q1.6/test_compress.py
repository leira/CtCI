#!/usr/bin/env python3

def compress(inStr):
    compressed = []
    curChar = ''
    count = 0

    for c in inStr:
        if c == curChar:
            count += 1
        else:
            if curChar != '':
                compressed.append(curChar)
                compressed.append(str(count))
            curChar = c
            count = 1

    compressed.append(curChar)
    compressed.append(str(count))

    if len(compressed) < len(inStr):
        return ''.join(compressed)
    else:
        return inStr


def test_compress():
    assert 'a2b1c5a3' == compress('aabcccccaaa')
    assert '13233245' == compress('1112223344444')
    assert 'abcd' == compress('abcd')
    assert 'aabbccdd' == compress('aabbccdd')

