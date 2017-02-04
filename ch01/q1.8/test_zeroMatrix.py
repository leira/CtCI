#!/usr/bin/env python3

def zeroRow(mat, r):
    for j in range(len(mat[r])):
        mat[r][j] = 0

def zeroCol(mat, c):
    for i in range(len(mat)):
        mat[i][c] = 0

def zeroMatrix(mat):
    zrow = set()
    zcol = set()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                zrow.add(i)
                zcol.add(j)
    for i in zrow:
        zeroRow(mat, i)
    for j in zcol:
        zeroCol(mat, j)

    return mat


def test_zeroMatrix():
    assert [[]] == zeroMatrix([[]])
    assert [[0]] == zeroMatrix([[0]])
    assert [[1]] == zeroMatrix([[1]])

    assert [[1, 0],
            [0, 0]] == zeroMatrix([[1, 1],
                                   [1, 0]])

    assert [[1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]] == zeroMatrix([[1, 1, 1],
                                      [1, 0, 1],
                                      [1, 1, 1]])

